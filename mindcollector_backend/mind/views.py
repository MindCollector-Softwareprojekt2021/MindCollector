from django.shortcuts import render

from django.http.response import JsonResponse
from django.core.files.storage import FileSystemStorage
from rest_framework.parsers import JSONParser
from rest_framework import status
import os
import logging
import json
from datetime import datetime
import easyocr
import speech_recognition

from mind.models import EINTRAG, USERACCOUNT, KATHEGORIE
from mind.serializers import UserSerializer, EintragSerializer, KathegorieSerializer
from rest_framework.decorators import api_view

# Einfache Registierung des Nutzers mit Bestätigung
@api_view(['POST'])
def mindcollector_register_user(request):
    if request.method == 'POST':
            user_data = JSONParser().parse(request)
            user_serializer = UserSerializer(data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                logging.info('mindcollector_register_user used by ' + user_data['USERNAME'] + " and registrated")
                return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
            logging.error('mindcollector_register_user used by ' + user_data['USERNAME'] + "and failed")
            return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Überprüfung mit der Datenbank nach Nutzername und Passwort
@api_view(['POST'])
def mindcollector_login(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user = USERACCOUNT.objects.get(pk=user_data['USERNAME'])
        if str(user.PASSWORT) == str(user_data['PASSWORT']) and str(user.USERNAME) == str(user_data['USERNAME']) :
            logging.info('mindcollector_login used by ' + user_data['USERNAME'] + " and logged in")
            return JsonResponse({'message': 'Logging in'}, status=status.HTTP_204_NO_CONTENT)
        logging.error('mindcollector_login used by ' + user_data['USERNAME'] + " and failed")
        return JsonResponse({'message': 'Locked!'}, status=status.HTTP_423_LOCKED)

# Lädt alle Inhalte des Nutzers nach der Erstellung sortiert vom Backend herunter
@api_view(['POST'])
def mindcollector_load(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        katego = KATHEGORIE.objects.order_by('-CREATED_AT')
        katego.filter(USERNAME=user_data['USERNAME'])
        ober_json =[]
        katego_json = {}
        for a in range(len(katego)):
            if user_data['USERNAME'] == str(katego[a].BESITZER):
                katego_json = {"KATEGORIE_ID":katego[a].id,
                                "KATEGORIE_TITEL":katego[a].KATEGORIE_TITEL,
                                "EINTRAG":[] }
                eintrag = EINTRAG.objects.order_by('-CREATED_AT')
                eintrag.filter(KATEGORIE=katego[a].id)
                for b in range(len(eintrag)):
                    if katego[a].id == eintrag[b].KATEGORIE_id:
                        if str(eintrag[b].BILD) !="":
                            katego_json["EINTRAG"].append({"EINTRAG_ID":eintrag[b].id, "EINTRAG_TITEL":eintrag[b].EINTRAG_TITEL, "EINTRAG_BESCHREIBUNG":eintrag[b].EINTRAG_BESCHREIBUNG, "EINTRAG_BILD":"http://mccurly.pythonanywhere.com" + eintrag[b].BILD})
                        else:
                            katego_json["EINTRAG"].append({"EINTRAG_ID":eintrag[b].id, "EINTRAG_TITEL":eintrag[b].EINTRAG_TITEL, "EINTRAG_BESCHREIBUNG":eintrag[b].EINTRAG_BESCHREIBUNG, "EINTRAG_BILD":""})
                ober_json.append(katego_json)
        logging.info('mindcollector_load used by ' + user_data['USERNAME'] + " and got " + json.dumps(ober_json))
        return JsonResponse(ober_json,safe=False, status=status.HTTP_200_OK)

# Legt eine Kategorie an mit den geschickten Informationen des Frontends in der Datenbank
@api_view(['POST'])
def mindcollector_kategorie(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        kathegorie_serializer = KathegorieSerializer(data={'KATEGORIE_TITEL': user_data['KATEGORIE_TITEL'], 'USERNAME':[str(user_data['USERNAME'])], 'BESITZER':str(user_data['USERNAME'])})
        if type(user_data['USERNAME']) == type(""):
            user_data['USERNAME'] = [user_data['USERNAME']]
        if kathegorie_serializer.is_valid():
            kathegorie_serializer.save()
            ka = KATHEGORIE.objects.last()
            logging.info('mindcollector_kategorie used by ' + str(user_data['USERNAME']) + " and sended " + json.dumps({"KATEGORIE_ID":ka.id,
                            "KATEGORIE_TITEL": ka.KATEGORIE_TITEL,
                            "EINTRAG":[]
                            }))
            return JsonResponse({"KATEGORIE_ID":ka.id,
                            "KATEGORIE_TITEL": ka.KATEGORIE_TITEL,
                            "EINTRAG":[]
                            }, safe=False, status=status.HTTP_201_CREATED)
        logging.error('mindcollector_kategorie used by ' + user_data['USERNAME'] + " and failed")
        return JsonResponse({'message': 'Kategorie not created!'}, status=status.HTTP_400_BAD_REQUEST)

# Löscht anhand der ID die Kategorie aus der Datenbank
@api_view(['POST'])
def mindcollector_kategorie_delete(request):
    if request.method == 'POST':
        kate_data = JSONParser().parse(request)
        print(kate_data)
        kate = KATHEGORIE.objects.get(id=kate_data['KATEGORIE_ID'])
        kate.delete()
        logging.info('mindcollector_kategorie_delete deleted ' + str(kate_data['KATEGORIE_ID']))
        return JsonResponse({'message': 'Kategorie deleted!'}, status=status.HTTP_204_NO_CONTENT)
    logging.error({'message': 'Kategorie not found!'})
    return JsonResponse({'message': 'Kategorie not found!'}, status=status.HTTP_400_BAD_REQUEST)

# Erstellt einen Eintrag mit der KategorieID für den jeweiligen User ohne Bild,Audio
# Updated jede Art von Eintrag
@api_view(['PUT','POST'])
def mindcollector_notiz(request):
    if request.method == 'POST':
        notiz_data = JSONParser().parse(request)
        data = {'KATEGORIE':notiz_data['KATEGORIE_ID'],
                    'EINTRAG_TITEL':notiz_data['EINTRAG']['EINTRAG_TITEL'],
                    'EINTRAG_BESCHREIBUNG':notiz_data['EINTRAG']['EINTRAG_BESCHREIBUNG'],
                    'BILD':notiz_data['EINTRAG']['EINTRAG_BILD'],
                    'CREATED_AT':datetime.now}
        eintrag_Serializer = EintragSerializer(data=data)
        if eintrag_Serializer.is_valid():
            eintrag_Serializer.save()
            logging.info('mindcollector_notiz used by ' + str(notiz_data['USERNAME']) + " and added " + notiz_data['EINTRAG']['EINTRAG_TITEL'])
            return JsonResponse({'message': 'Notiz'}, status=status.HTTP_200_OK)
        logging.error(eintrag_Serializer.errors)
        return JsonResponse({'message': 'Locked!'}, status=status.HTTP_423_LOCKED)
    elif request.method == 'PUT':
        notiz_data = JSONParser().parse(request)
        notizen = EINTRAG.objects.all()
        no = notizen.get(id=notiz_data['EINTRAG_ID'])
        if "EINTRAG_BILD" in notiz_data:
            data = {'KATEGORIE':no.KATEGORIE_id,
                    'id':notiz_data['EINTRAG_ID'],
                    'EINTRAG_TITEL':notiz_data['EINTRAG_TITEL'],
                    'EINTRAG_BESCHREIBUNG':notiz_data['EINTRAG_BESCHREIBUNG'],
                    'BILD':notiz_data['EINTRAG_BILD']}
            eintrag_Serializer = EintragSerializer(data=data)
            EINTRAG.objects.filter(id=notiz_data['EINTRAG_ID']).update(EINTRAG_TITEL=notiz_data['EINTRAG_TITEL'], EINTRAG_BESCHREIBUNG=notiz_data['EINTRAG_BESCHREIBUNG'], BILD=notiz_data['EINTRAG_BILD'])
        elif "EINTRAG_Audio" in notiz_data:
            data = {'KATEGORIE':no.KATEGORIE_id,
                    'id':notiz_data['EINTRAG_ID'],
                    'EINTRAG_TITEL':notiz_data['EINTRAG_TITEL'],
                    'EINTRAG_BESCHREIBUNG':notiz_data['EINTRAG_BESCHREIBUNG'],
                    'AUDIO':notiz_data['EINTRAG_AUDIO']}
            eintrag_Serializer = EintragSerializer(data=data)
            EINTRAG.objects.filter(id=notiz_data['EINTRAG_ID']).update(EINTRAG_TITEL=notiz_data['EINTRAG_TITEL'], EINTRAG_BESCHREIBUNG=notiz_data['EINTRAG_BESCHREIBUNG'], AUDIO=notiz_data['EINTRAG_AUDIO'])
        else:
            data = {'KATEGORIE':no.KATEGORIE_id,
                    'id':notiz_data['EINTRAG_ID'],
                    'EINTRAG_TITEL':notiz_data['EINTRAG_TITEL'],
                    'EINTRAG_BESCHREIBUNG':notiz_data['EINTRAG_BESCHREIBUNG']}
            eintrag_Serializer = EintragSerializer(data=data)
            EINTRAG.objects.filter(id=notiz_data['EINTRAG_ID']).update(EINTRAG_TITEL=notiz_data['EINTRAG_TITEL'], EINTRAG_BESCHREIBUNG=notiz_data['EINTRAG_BESCHREIBUNG'])
        logging.info('mindcollector_notiz used updated ' + notiz_data['EINTRAG_TITEL'])
        return JsonResponse({'message': 'Eintrag updated!'}, status=status.HTTP_200_OK)


# Erstellt eine Analyse eines übergeben Bildes, welches sich auf dem Fileserver befindet
def bild_analyse(file, last):
    try:
        last_id = last.id
        path="/home/McCurly/mindcollector/media/"+file
        logging.info('Ananlyse START: '+path)
        with open(path, 'rb') as data:
            image = data.read()
        reader = easyocr.Reader(['de'], gpu=False)
        results = reader.readtext(image)
        text = ''
        for result in results:
            text += result[1]+' '
        logging.info('bild_analyse used. Result: ' + str(text))
        EINTRAG.objects.filter(id=last_id).update(EINTRAG_BESCHREIBUNG=text)
    except FileNotFoundError as e:
        logging.warning(e)
        EINTRAG.objects.filter(id=last_id).update(EINTRAG_BESCHREIBUNG="Leider ist ein Fehler bei der Analyse aufgetreten.")

# Erstellt einen Eintrag mit der KategorieID für den jeweiligen User mit Bild
@api_view(['POST'])
def mindcollector_notiz_bild(request):
    if request.method == 'POST':
        files = request.FILES.get('EINTRAG_BILD', False)
        fs = FileSystemStorage()
        filename = fs.save(files.name, files)
        uploaded_file_url = fs.url(filename)
        if request.POST.get('EINTRAG_BESCHREIBUNG', False):
            data = {'KATEGORIE':request.POST['KATEGORIE_ID'],
                        'EINTRAG_TITEL':request.POST['EINTRAG_TITEL'],
                        'EINTRAG_BESCHREIBUNG':request.POST['EINTRAG_BESCHREIBUNG'],
                        'BILD':uploaded_file_url,
                        'CREATED_AT':datetime.now}
            eintrag_Serializer = EintragSerializer(data=data)
            if eintrag_Serializer.is_valid():
                eintrag_Serializer.save()
        else:
            data = {'KATEGORIE':request.POST['KATEGORIE_ID'],
                        'EINTRAG_TITEL':request.POST['EINTRAG_TITEL'],
                        'EINTRAG_BESCHREIBUNG':'Bild wird analysiert.... Das kann einige Minuten dauern.',
                        'BILD':uploaded_file_url,
                        'CREATED_AT':datetime.now}
            eintrag_Serializer = EintragSerializer(data=data)
            if eintrag_Serializer.is_valid():
                eintrag_Serializer.save()
                ein = EINTRAG.objects.last()
                bild_analyse(filename, ein)

        logging.info("mindcollector_notiz_bild used and added " + request.POST['EINTRAG_TITEL'])
        return JsonResponse({'message': 'Notiz mit Bild'}, status=status.HTTP_200_OK)
    logging.error(eintrag_Serializer.errors)
    return JsonResponse({'message': 'Notiz mit Bild'}, status=status.HTTP_400_BAD_REQUEST)


# Analysiert eine übergebene Audiodatei und Updated den dazugehörigen Eintrag
def audio_analyse(file, ein):
    last_id = ein.id
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.AudioFile("/home/McCurly/mindcollector/media/" + file) as source:
        text=""
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="de-DE")
        except speech_recognition.UnknownValueError as e:
            logging.warning(e)
        logging.info('audio_analyse used. Result: ' + str(text))

    EINTRAG.objects.filter(id=last_id).update(EINTRAG_BESCHREIBUNG=text)


# Erstellt einen Eintrag mit der KategorieID für den jeweiligen User mit Audio
@api_view(['PUT','POST'])
def mindcollector_notiz_audio(request):
    if request.method == 'POST':
        files = request.FILES.get('AUDIO', False)
        fs = FileSystemStorage()
        filename = fs.save("Audio", files)
        data = {'KATEGORIE':request.POST['KATEGORIE_ID'],
                    'EINTRAG_TITEL':request.POST['EINTRAG_TITEL'],
                    'EINTRAG_BESCHREIBUNG': "Audio wird analysiert..."}
        eintrag_Serializer = EintragSerializer(data=data)
        if eintrag_Serializer.is_valid():
            eintrag_Serializer.save()
            ein = EINTRAG.objects.last()
            audio_analyse(filename, ein)

            logging.info('mindcollector_notiz_audio used and added ' + request.POST['EINTRAG_TITEL'])
            return JsonResponse({'message': 'Notiz mit Audio'}, status=status.HTTP_200_OK)
    logging.error(eintrag_Serializer.errors)
    return JsonResponse({'message': 'Notiz mit Audio'}, status=status.HTTP_400_BAD_REQUEST)


# Löscht einen Eintrag, falls vorhanden, werden Bilder/Audiodatein mit gelöscht
@api_view(['POST'])
def mindcollector_notiz_delete(request):
    if request.method == 'POST':
        eintrag_data = JSONParser().parse(request)
        eintrag = EINTRAG.objects.get(id=eintrag_data['EINTRAG_ID'])
        try:
            if eintrag.BILD != "":
                os.remove("/home/McCurly/mindcollector" + eintrag.BILD)
            if eintrag.AUDIO != "":
                os.remove("/home/McCurly/mindcollector" + eintrag.AUDIO)
        except FileNotFoundError as e:
            logging.warning(e)
        eintrag.delete()
        logging.info('mindcollector_notiz_delete used and deleted ' + str(eintrag_data['EINTRAG_ID']))
        return JsonResponse({'message': 'Eintrag deleted!'}, status=status.HTTP_204_NO_CONTENT)
    logging.error({'message': 'Eintrag not found!'})
    return JsonResponse({'message': 'Eintrag not found!'}, status=status.HTTP_400_BAD_REQUEST)