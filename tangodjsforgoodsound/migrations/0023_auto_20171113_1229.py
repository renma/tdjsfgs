# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-13 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tangodjsforgoodsound', '0022_auto_20171106_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dj',
            name='number_of_milongas',
            field=models.IntegerField(blank=True, choices=[(0, 0), (10, 10), (20, 20), (30, 30), (40, 40), (50, 50), (60, 60), (70, 70), (80, 80), (90, 90), (100, 100), (110, 110), (120, 120), (130, 130), (140, 140), (150, 150), (160, 160), (170, 170), (180, 180), (190, 190), (200, 200), (210, 210), (220, 220), (230, 230), (240, 240), (250, 250), (260, 260), (270, 270), (280, 280), (290, 290), (300, 300), (350, 350), (400, 400), (450, 450), (500, 500), (550, 550), (600, 600), (650, 650), (700, 700), (750, 750), (800, 800), (850, 850), (900, 900), (950, 950), (1000, 1000), (1200, 1200), (1400, 1400), (1600, 1600), (1800, 1800), (2000, 2000)], default=0, verbose_name='Number of milongas'),
        ),
    ]