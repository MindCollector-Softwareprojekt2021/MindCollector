from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from mindcollector.models import EINTRAG, USERACCOUNT, KATHEGORIE
from mindcollector.serializers import MindcollectorSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def mindcollector_list_user(request):
    if request.method == 'GET':
        users = USERACCOUNT.objects.all()
        mindcollectorSerializer = MindcollectorSerializer(users, many=True)
        return JsonResponse(mindcollectorSerializer.data, safe=False)
    elif request.method == 'POST':
            mindcollector_data = JSONParser().parse(request)
            mindcollector_serializer = MindcollectorSerializer(data=mindcollector_data)
            if mindcollector_serializer.is_valid():
                mindcollector_serializer.save()
                return JsonResponse(mindcollector_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(mindcollector_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def mindcollector_list_user_details(request, pk):
    user = USERACCOUNT.objects.get(pk=pk)
    if request.method == 'GET':
        tutorial_serializer = MindcollectorSerializer(user)
        return JsonResponse(tutorial_serializer.data)
    elif request.method == 'PUT':
            mindcollector_data = JSONParser().parse(request)
            mindcollector_serializer = MindcollectorSerializer(user, data=mindcollector_data)
            if mindcollector_serializer.is_valid():
                mindcollector_serializer.save()
                return JsonResponse(mindcollector_serializer.data)
            return JsonResponse(mindcollector_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

