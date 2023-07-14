from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("save_speech_to_text/", views.save_speech_to_text, name="save_speech_to_text")
]
