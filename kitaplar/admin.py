from django.contrib import admin
from .models import Yorum, Kitap
# Register your models here.


@admin.register(Kitap)
class KitapAdmin(admin.ModelAdmin):
    list_display = ('isim', 'yazar', 'yaratilma_tarihi')
    list_display_links = ('isim', 'yazar', 'yaratilma_tarihi')


@admin.register(Yorum)
class YorumAdmin(admin.ModelAdmin):
    list_display = ('yorum_sahibi', 'yaratilma_tarihi', 'kitap')
    list_display_links = ('yorum_sahibi', 'yaratilma_tarihi', 'kitap')
