from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.FeminosalistView.as_view(), name='draga_list'),
    path('create/', views.FeminosacreateView.as_view(), name='draga_create'),
]
