# Generated by Django 3.1.7 on 2021-02-20 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IGA', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=50),
        ),
    ]
