# Generated by Django 3.2 on 2021-04-20 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0009_remove_userresps_pontuacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='nome2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='musica',
            name='nome3',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='musica',
            name='nome4',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
