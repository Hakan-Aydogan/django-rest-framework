from django.shortcuts import get_object_or_404
from .serializers import Kitapserializer, YorumSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from ..models import Kitap, Yorum
from kitaplar.api.permisions import IsAdminUserOrReadOnly


class KitapListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kitap.objects.all()
    serializer_class = Kitapserializer
    permission_classes = [IsAdminUserOrReadOnly]


class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitap.objects.all()
    serializer_class = Kitapserializer
    permission_classes = [IsAdminUserOrReadOnly]


class YorumCreateAPIView(generics.CreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer

    def perform_create(self, serializer):
        kitap_pk = self.kwargs.get('kitap_pk')
        kitap = get_object_or_404(Kitap, pk=kitap_pk)
        serializer.save(kitap=kitap)


class YorumListAPIView(generics.ListAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer


class YorumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer


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
