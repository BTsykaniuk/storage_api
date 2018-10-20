from django.urls import path
from api import views


urlpatterns = [
    path('', views.ItemListAPIView.as_view(), name='list'),
    path('create/', views.ItemsCreateAPIView.as_view(), name='create'),
    path('update/<int:pk>/', views.ItemsUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ItemsDeleteAPIView.as_view(), name='delete'),
    path('sellers/', views.SellerListAPIView.as_view(), name='sellers'),
]
