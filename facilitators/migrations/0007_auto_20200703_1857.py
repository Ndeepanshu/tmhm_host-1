# Generated by Django 3.0.7 on 2020-07-03 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilitators', '0006_auto_20200703_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilitator',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
