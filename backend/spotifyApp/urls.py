from django.urls import path
from . import views

urlpatterns = [
    #path("",views.getToken, name="tokenInit"),
    path("",views.handlePost, name="SpotifyQuery")
]