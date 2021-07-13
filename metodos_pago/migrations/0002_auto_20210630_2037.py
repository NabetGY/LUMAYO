# Generated by Django 3.1.7 on 2021-07-01 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metodos_pago', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarjeta',
            name='fec_expiracion',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='saldo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
