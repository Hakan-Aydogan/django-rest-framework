from django.contrib import admin
from django.urls import path, include
from kitaplar.api import views as api_views

urlpatterns = [
    path('kitaplar/', api_views.KitapListCreateAPIView.as_view(), name='kitaplar'),
    path('kitaplar/<int:pk>', api_views.KitapDetailAPIView.as_view(),
         name='kitap'),
    path('kitaplar/<int:kitap_pk>/yorum-yap', api_views.YorumCreateAPIView.as_view(),
         name='yorum-yap'),
    path('yorumlar/', api_views.YorumListAPIView.as_view(), name='yorumlar'),
    path('yorumlar/<int:pk>', api_views.YorumDetailAPIView.as_view(), name='yorum'),

]
