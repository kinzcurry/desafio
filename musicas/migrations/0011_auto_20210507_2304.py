# Generated by Django 3.2 on 2021-05-08 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0010_auto_20210420_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='musica',
            name='dica',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='userresps',
            name='dicas',
            field=models.BooleanField(default=False),
        ),
    ]
