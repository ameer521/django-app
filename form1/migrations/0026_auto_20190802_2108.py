# Generated by Django 2.2.2 on 2019-08-02 15:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0025_auto_20190802_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='cdt',
            field=models.DateTimeField(auto_now=True, verbose_name='Date Time Field'),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='cdate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='DateField'),
        ),
    ]
