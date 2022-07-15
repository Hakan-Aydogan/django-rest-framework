# Generated by Django 4.0.6 on 2022-07-15 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kitaplar', '0002_alter_yorum_yorum_sahibi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yorum',
            name='yorum_sahibi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorum_yapan', to=settings.AUTH_USER_MODEL),
        ),
    ]
