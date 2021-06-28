from django.conf.urls import url
from mind import views

urlpatterns = [
    url(r'^api/user', views.mindcollector_register_user),
    url(r'^api/login', views.mindcollector_login),
    url(r'^api/load', views.mindcollector_load),
    url(r'^api/kategorie', views.mindcollector_kategorie),
    url(r'^api/deleteKategorie', views.mindcollector_kategorie_delete),
    url(r'^api/notiz', views.mindcollector_notiz),
    url(r'^api/bildNotiz', views.mindcollector_notiz_bild),
    url(r'^api/audioNotiz', views.mindcollector_notiz_audio),
    url(r'^api/deleteNotiz', views.mindcollector_notiz_delete)
]