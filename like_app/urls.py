from django.urls import path
from like_app import views

urlpatterns = [
    path('', views.main_index, name="main_index"),
]
