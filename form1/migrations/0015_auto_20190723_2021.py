# Generated by Django 2.2.2 on 2019-07-23 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0014_auto_20190723_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='hello')),
            ],
        ),
        migrations.AlterModelOptions(
            name='testmodel',
            options={},
        ),
    ]