# Generated by Django 4.0.6 on 2022-07-10 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasktable',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
