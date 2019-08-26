# Generated by Django 2.2.2 on 2019-07-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0017_auto_20190723_2029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testmodel',
            options={'verbose_name': 'PostTest', 'verbose_name_plural': 'posting'},
        ),
        migrations.AddField(
            model_name='testmodel',
            name='publish',
            field=models.CharField(choices=[('foot', 'Football'), ('cri', 'Cricket'), ('bas', 'Basketball')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='title',
            field=models.CharField(default='hello', max_length=20, verbose_name='Post model'),
        ),
    ]