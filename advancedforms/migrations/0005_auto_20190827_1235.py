# Generated by Django 2.2.4 on 2019-08-27 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advancedforms', '0004_formmodel_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formmodel',
            name='img',
        ),
        migrations.AddField(
            model_name='formmodel',
            name='file',
            field=models.FileField(blank=True, upload_to='media'),
        ),
    ]
