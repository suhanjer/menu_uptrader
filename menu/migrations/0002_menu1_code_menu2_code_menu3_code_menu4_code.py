# Generated by Django 4.2 on 2023-04-26 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu1',
            name='code',
            field=models.CharField(default='1', max_length=64),
        ),
        migrations.AddField(
            model_name='menu2',
            name='code',
            field=models.CharField(default='1', max_length=64),
        ),
        migrations.AddField(
            model_name='menu3',
            name='code',
            field=models.CharField(default='1', max_length=64),
        ),
        migrations.AddField(
            model_name='menu4',
            name='code',
            field=models.CharField(default='1', max_length=64),
        ),
    ]
