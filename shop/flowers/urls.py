from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('detail-view/<int:pk>', views.detail_view, name='detail'),
    path('deleteflower/<int:pk>', views.delete_flower, name='delete'),
    path('delete_all/', views.delete_all, name='delete_all'),
    path('create_new/', views.create_new, name='create_new')

]
