from django.urls import path
from api import views


urlpatterns = [
    path('create/', views.ProductsCreateAPIView.as_view(), name='create'),
    path('update/', views.ProductUpdateAPIView.as_view(), name='update'),
    path('delete/', views.ProductDeleteAPIView.as_view(), name='delete')
]
