# Generated by Django 3.1.7 on 2021-02-20 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IGA', '0002_auto_20210221_0145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='img',
            new_name='image',
        ),
    ]
