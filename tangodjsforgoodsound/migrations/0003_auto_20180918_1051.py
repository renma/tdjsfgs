# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 10:51


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tangodjsforgoodsound', '0002_auto_20180303_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dj',
            name='favorites',
            field=models.CharField(blank=True, default='', max_length=300, verbose_name='Favored orchestras'),
        ),
    ]
