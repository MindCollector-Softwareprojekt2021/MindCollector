from django.db import models

class USERACCOUNT(models.Model):
    benutzername = models.BigAutoField(serialize=False, primary_key=True, verbose_name='benutzer')
    full_name = models.CharField(max_length=50, blank=False, default='')
    passwort = models.CharField(max_length=50, blank=False, default='')
    sicherheitsfrage1 = models.TextField(blank=False, default='')
    sicherheitsanwort1 = models.TextField(blank=False, default='')
    sicherheitsfrage2 = models.TextField(blank=False, default='')
    sicherheitsanwort2 = models.TextField(blank=False, default='')
    created_at = models.TimeField(auto_now=True)

class KATHEGORIE(models.Model):
    user = models.ManyToManyField(USERACCOUNT)
    kathegorie_titel = models.CharField(max_length=50, blank=False, default='')

class EINTRAG(models.Model):
    kathegorie = models.ForeignKey(KATHEGORIE, on_delete=models.CASCADE)
    eintrag_titel = models.CharField(max_length=50, blank=False, default='')
    eintrag_beschreibung = models.TextField(blank=False, default='')
    audio = models.FileField(blank=True)
    audiotext = models.TextField(blank=True, default='')
    bild = models.ImageField(blank=True)


