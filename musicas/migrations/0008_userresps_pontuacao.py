# Generated by Django 3.2 on 2021-04-19 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0007_auto_20210418_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresps',
            name='pontuacao',
            field=models.IntegerField(default=0),
        ),
    ]
