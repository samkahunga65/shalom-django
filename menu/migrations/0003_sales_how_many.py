# Generated by Django 2.2.5 on 2020-03-07 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20200307_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='how_many',
            field=models.IntegerField(default=1),
        ),
    ]