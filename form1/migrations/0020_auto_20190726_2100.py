# Generated by Django 2.2.2 on 2019-07-26 15:30

from django.db import migrations, models
import form1.models


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0019_auto_20190726_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='author_email',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, validators=[form1.models.validate_email], verbose_name='email'),
        ),
    ]
