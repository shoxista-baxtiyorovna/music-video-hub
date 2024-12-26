from django.urls import path
from . import views



app_name = 'tracks'

urlpatterns = [
    path('list/', views.track_list, name='list'),
    path('create/', views.track_create, name='create'),
    path('update/<int:track_id>/', views.update, name='update'),
    path('delete/<int:track_id>/', views.track_delete, name='delete'),
    path('detail/<int:track_id>/', views.detail, name='detail'),
]