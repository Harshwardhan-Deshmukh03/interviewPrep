# Generated by Django 4.2.2 on 2024-04-02 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_resource'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]