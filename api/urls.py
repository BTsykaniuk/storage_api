from django.urls import path
from api import views


urlpatterns = [
    path('', views.ItemListAPIView.as_view(), name='list'),
    path('create/', views.ItemsCreateAPIView.as_view(), name='create'),
    path('update/', views.ItemsUpdateAPIView.as_view(), name='update'),
    path('delete/', views.ItemsDeleteAPIView.as_view(), name='delete'),
    path('sellers/', views.ItemsDeleteAPIView.as_view(), name='sellers'),
]
