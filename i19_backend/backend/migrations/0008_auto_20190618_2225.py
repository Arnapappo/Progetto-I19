# Generated by Django 2.2.2 on 2019-06-18 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20190618_2110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prodottoordinato',
            old_name='id_tavolo',
            new_name='idTavolo',
        ),
    ]
