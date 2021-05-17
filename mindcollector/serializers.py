from rest_framework import serializers
from mindcollector.models import *


class MindcollectorSerializer(serializers.ModelSerializer):
    class MetaUser:
        model = USERACCOUNT
        fields = ('benutzername',
                  'full_name',
                  'email',
                  'passwort',
                  'sicherheitsfrage1',
                  'sicherheitsanwort1',
                  'sicherheitsfrage2',
                  'sicherheitsanwort2',
                  'created_at')

    class MetaEintrag:
        model = EINTRAG
        fields = ('eintrag',
                  'eintrag_titel',
                  'eintrag_beschreibung',
                  'audio',
                  'audiotext',
                  'bild',
                  'kathegorie')

    class MetaKathegorie:
        model = KATHEGORIE
        fields = ('eintrag',
                  'kathegorie_titel',
                  'user')
