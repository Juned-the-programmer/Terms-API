from django.urls import path
from . import views

urlpatterns = [
    path('list_api/',views.list_api,name="list_api"),
    path('text_extract/',views.text_extract,name="text_Extract"),
    path('text_process/',views.text_process,name="text_process")
]
