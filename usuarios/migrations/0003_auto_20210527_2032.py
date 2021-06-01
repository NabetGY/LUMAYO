# Generated by Django 3.1.7 on 2021-05-28 01:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], default='O', max_length=20),
        ),
        migrations.CreateModel(
            name='Preferencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferencia', models.CharField(choices=[('terror', 'terror'), ('drama', 'drama'), ('ficcion', 'ficcion')], default='terror', max_length=20)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
