# Generated by Django 2.0.12 on 2019-04-07 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20190406_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='maximum_marks',
            field=models.IntegerField(default=500),
        ),
        migrations.AlterField(
            model_name='question',
            name='minimum_marks',
            field=models.IntegerField(default=0),
        ),
    ]
