# Generated by Django 3.2 on 2021-04-17 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musicas', '0003_musica_acertou'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respostas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserResps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respostas_lista', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='musicas.respostas')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
