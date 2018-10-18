from django.urls import path
from api import views


urlpatterns = [
    path('create/', views.ItemsCreateAPIView.as_view(), name='create'),
    path('update/', views.ItemsUpdateAPIView.as_view(), name='update'),
    path('delete/', views.ItemsDeleteAPIView.as_view(), name='delete')
]
