from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^main$', views.main),
    url(r'^event$', views.event),
    url(r'^alert$', views.alert),
]
