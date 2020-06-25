# Generated by Django 3.0.6 on 2020-05-31 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('trainer_id', models.AutoField(primary_key=True, serialize=False)),
                ('tname', models.CharField(default='', max_length=50)),
                ('temail', models.CharField(default='', max_length=30)),
                ('tphone', models.CharField(default='', max_length=10)),
                ('exp', models.CharField(default='', max_length=1000)),
                ('texp', models.CharField(default='', max_length=1000)),
                ('tprofile', models.CharField(default='', max_length=1000)),
                ('file', models.FileField(default='', upload_to='facilitators/profile')),
            ],
        ),
    ]