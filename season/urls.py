from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.SeasonListView.as_view(), name='season_list'),
    path('create/', views.SeasonCreateView.as_view(), name='season_create'),
    path('<int:pk>/chapters/', views.ChapterListView.as_view(), name='chapter_list'),
    path('<int:pk>/chapters/create/', views.ChapterCreateView.as_view(), name='chapter_create'),
    path('<int:pk>/draga-data/create/', views.DragaDataCreateView.as_view(), name='draga_data_create'),
]
