# Generated by Django 2.2.2 on 2019-08-05 15:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0027_testmodel_tstamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='udt',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated '),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='cdt',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='CreatedDate'),
        ),
    ]
