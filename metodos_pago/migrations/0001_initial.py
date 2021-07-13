# Generated by Django 3.1.7 on 2021-06-30 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import metodos_pago.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=19)),
                ('nombre_apellido', models.CharField(max_length=200)),
                ('fec_expiracion', models.DateField()),
                ('cvc', models.CharField(max_length=3)),
                ('defecto', models.BooleanField(default=False)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.CharField(choices=[(metodos_pago.models.TipoTarjeta['DEBITO'], 'DEBITO'), (metodos_pago.models.TipoTarjeta['CREDITO'], 'CREDITO')], default=metodos_pago.models.TipoTarjeta['CREDITO'], max_length=8)),
                ('saldo', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
