# Generated by Django 2.1.3 on 2018-11-09 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0003_auto_20181109_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]