# Generated by Django 3.2 on 2021-04-16 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0002_musica_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='acertou',
            field=models.BooleanField(default=False),
        ),
    ]
