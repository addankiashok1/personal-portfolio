# Generated by Django 3.1.6 on 2021-02-07 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210207_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allblogs',
            name='description',
            field=models.TextField(max_length=1500),
        ),
    ]
