from django.urls import path

from . import views

urlpatterns = [
    path('', views.gameView, name='gameView'),
    path('<slug:name>', views.gameSpecificView, name='gameSpecificView'),
    path('<slug:name>/beforegame', views.beforeGameView, name='beforeGameView'),
    ]