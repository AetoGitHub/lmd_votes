from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.Home.as_view(), name='home'),
    path('nuevo/', views.MensajeCreateView.as_view(), name='mensaje_nuevo'),
    path('lista/', views.MensajeListView.as_view(), name='mensaje_lista'),
]
