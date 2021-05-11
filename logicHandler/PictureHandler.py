import ssl
import easyocr

ssl._create_default_https_context = ssl._create_unverified_context

def getPictureText(path):
    reader = easyocr.Reader(['de', 'en'], gpu=False)

    results = reader.readtext(path)

    text = ''

    for result in results:
        text += result[1]+' '

    return text
