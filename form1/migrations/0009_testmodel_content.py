# Generated by Django 2.2.2 on 2019-07-22 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0008_auto_20190722_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='content',
            field=models.TextField(null=True),
        ),
    ]