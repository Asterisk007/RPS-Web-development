# Generated by Django 2.2.5 on 2020-05-06 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20200503_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='completed_rounds',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='game',
            name='max_rounds',
            field=models.IntegerField(default=1),
        ),
    ]