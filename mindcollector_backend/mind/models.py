from django.db import models
from datetime import datetime

class USERACCOUNT(models.Model):
    USERNAME = models.CharField(max_length=254, serialize=False, primary_key=True, verbose_name='ID')
    FULL_NAME = models.CharField(max_length=254, blank=False, default='')
    PASSWORT = models.CharField(max_length=254, blank=False, default='')
    SICHERHEITSFRAGE1 = models.TextField(blank=False, default='')
    SICHERHEITSFRAGE2 = models.TextField(blank=False, default='')
    SICHERHEITSANTWORT1 = models.TextField(blank=False, default='')
    SICHERHEITSANTWORT2 = models.TextField(blank=False, default='')

class KATHEGORIE(models.Model):
    KATEGORIE_TITEL = models.CharField(max_length=254, blank=False, default='')
    USERNAME = models.ManyToManyField(USERACCOUNT)
    BESITZER = models.TextField(blank=True, default='')
    CREATED_AT = models.DateTimeField(auto_now_add=True)

class EINTRAG(models.Model):
    KATEGORIE = models.ForeignKey(KATHEGORIE, on_delete=models.CASCADE)
    EINTRAG_TITEL = models.CharField(max_length=254, blank=False, default='')
    EINTRAG_BESCHREIBUNG = models.TextField(blank=False, default='')
    AUDIO = models.TextField(blank=True, default='')
    AUDIOTEXT = models.TextField(blank=True, default='')
    BILD = models.TextField(blank=True, default='')
    CREATED_AT = models.DateTimeField(default=datetime.now)