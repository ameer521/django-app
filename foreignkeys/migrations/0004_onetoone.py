# Generated by Django 2.2.4 on 2019-08-30 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foreignkeys', '0003_manytomany_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Onetoone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(max_length=25, null=True)),
                ('user', models.OneToOneField(default='admin', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]