# Generated by Django 3.2 on 2021-04-18 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0004_respostas_userresps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresps',
            name='respostas_lista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='musicas.musica'),
        ),
        migrations.DeleteModel(
            name='Respostas',
        ),
    ]
