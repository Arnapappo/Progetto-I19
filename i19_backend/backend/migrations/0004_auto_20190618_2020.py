# Generated by Django 2.2.2 on 2019-06-18 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20190618_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodottoordinato',
            name='tempoInizioLavorazione',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
