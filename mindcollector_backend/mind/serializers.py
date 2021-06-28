from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.USERACCOUNT
        fields = ('USERNAME',
                  'FULL_NAME',
                  'PASSWORT',
                  'SICHERHEITSFRAGE1',
                  'SICHERHEITSFRAGE2',
                  'SICHERHEITSANTWORT1',
                  'SICHERHEITSANTWORT2')

class EintragSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EINTRAG
        fields = ('id',
                  'EINTRAG_TITEL',
                  'EINTRAG_BESCHREIBUNG',
                  'AUDIO',
                  'AUDIOTEXT',
                  'BILD',
                  'KATEGORIE')

class KathegorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.KATHEGORIE
        fields = ('KATEGORIE_TITEL',
                  'USERNAME',
                  'BESITZER')
