# Generated by Django 4.0.6 on 2022-07-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0006_alter_tasktable_mtime_alter_tasktable_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasktable',
            name='mtime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
