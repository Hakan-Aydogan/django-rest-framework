from django.shortcuts import get_object_or_404
from .serializers import Kitapserializer, YorumSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from ..models import Kitap, Yorum
from kitaplar.api.permissions import IsAdminUserOrReadOnly, IsYorumSahibiOrReadOnly
from rest_framework.validators import ValidationError
from kitaplar.api.paginations import LargeResultsSetPagination, StandardResultsSetPagination


class KitapListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kitap.objects.all()
    serializer_class = Kitapserializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = StandardResultsSetPagination


class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitap.objects.all()
    serializer_class = Kitapserializer
    permission_classes = [IsAdminUserOrReadOnly]


class YorumCreateAPIView(generics.CreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        kitap_pk = self.kwargs.get('kitap_pk')
        kitap = get_object_or_404(Kitap, pk=kitap_pk)
        kullanici = self.request.user
        yorumlar = Yorum.objects.filter(kitap=kitap, yorum_sahibi=kullanici)
        if yorumlar.exists():
            raise ValidationError(
                'Bir kullanıcı 1 kitaba sadece 1 kere yorum yapabilir')

        serializer.save(kitap=kitap, yorum_sahibi=kullanici)


class YorumListAPIView(generics.ListAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class YorumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [IsYorumSahibiOrReadOnly]


""" class KitapListCreateApiView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Kitap.objects.all()
    serializer_class = Kitapserializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class YorumListCreateApiView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
 """
