from django.conf.urls import url
from mindcollector import views

urlpatterns = [
    url(r'^api/user', views.mindcollector_list_user),
    url(r'^api/user/(?P<pk>[0-9]+)$', views.mindcollector_list_user_details)
]