# Generated by Django 2.2.4 on 2019-08-30 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foreignkeys', '0006_auto_20190830_1133'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fromothermodel',
            new_name='From_other_model',
        ),
        migrations.RenameModel(
            old_name='Manytomany',
            new_name='Many_to_many',
        ),
        migrations.RenameModel(
            old_name='Onetoone',
            new_name='One_to_one',
        ),
        migrations.CreateModel(
            name='For_On_Delete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_null', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]