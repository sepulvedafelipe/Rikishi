# Generated by Django 2.1.2 on 2019-06-04 19:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0003_auto_20190604_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_pedido',
            name='cliente',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='detalle_pedido',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
