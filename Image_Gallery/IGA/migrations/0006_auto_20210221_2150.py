# Generated by Django 3.1.7 on 2021-02-21 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IGA', '0005_auto_20210221_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.CharField(choices=[('nature', 'Nature'), ('animals', 'Animals'), ('fruits', 'Fruits')], default='nature', max_length=50),
        ),
    ]