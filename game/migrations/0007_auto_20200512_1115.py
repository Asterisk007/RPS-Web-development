# Generated by Django 2.2.5 on 2020-05-12 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20200512_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='player2',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player2', to=settings.AUTH_USER_MODEL),
        ),
    ]