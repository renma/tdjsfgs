# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-24 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tangodjsforgoodsound', '0006_auto_20190114_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dj',
            name='audioformat',
            field=models.CharField(blank=True, choices=[(b'AIFF', 'AIFF Audio Interchange File Format (.aiff, aif)'), (b'FLAC', 'FLAC Free Lossless Audio Codec (.flac, .fla)'), (b'WAV', 'WAV Resource Interchange File Format (.wav)'), (b'ADA', 'ADA Advanced Digital Audio (.ada)'), (b'ALAC', 'ALAC Apple Lossless Audio Codec (.m4a, .mp4)'), (b'APE', "APE Monkey's Audio (.ape, .mac)"), (b'SHN', 'SHN Shorten (.shn)'), (b'TTA', 'TTA The True Audio (.tta)'), (b'WV', 'WV WavPack LOSSLESS (.wv)'), (b'ANALOG', 'ANALOG Playback of LPs/Shellacs')], default='', max_length=100, verbose_name='Main audio format'),
        ),
        migrations.AlterField(
            model_name='dj',
            name='audioformat2',
            field=models.CharField(blank=True, choices=[(b'AIFF', 'AIFF Audio Interchange File Format (.aiff, aif)'), (b'FLAC', 'FLAC Free Lossless Audio Codec (.flac, .fla)'), (b'WAV', 'WAV Resource Interchange File Format (.wav)'), (b'ADA', 'ADA Advanced Digital Audio (.ada)'), (b'ALAC', 'ALAC Apple Lossless Audio Codec (.m4a, .mp4)'), (b'APE', "APE Monkey's Audio (.ape, .mac)"), (b'SHN', 'SHN Shorten (.shn)'), (b'TTA', 'TTA The True Audio (.tta)'), (b'WV', 'WV WavPack LOSSLESS (.wv)'), (b'ANALOG', 'ANALOG Playback of LPs/Shellacs')], default='', max_length=100, verbose_name='Alternative audio format'),
        ),
        migrations.AlterField(
            model_name='dj',
            name='last_changed',
            field=models.DateField(auto_now=True, verbose_name='Last change'),
        ),
        migrations.AlterField(
            model_name='dj',
            name='since',
            field=models.IntegerField(blank=True, choices=[(2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980)], default=0, verbose_name='Since'),
        ),
    ]