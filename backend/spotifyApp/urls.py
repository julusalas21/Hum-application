from django.urls import path
from . import views

urlpatterns = [
    path("",views.getToken, name="check"),
    #path("",views.home, name="mainMetod")
]