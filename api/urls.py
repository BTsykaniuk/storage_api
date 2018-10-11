from django.urls import path
from api import views


urlpatterns = [
    path('', views.ProductListAPIView.as_view(), name='list'),
    # path('create/', views.ProductListAPIView.as_view(), name='create'),
    # path('update/', views.ProductListAPIView.as_view(), name='update')
]