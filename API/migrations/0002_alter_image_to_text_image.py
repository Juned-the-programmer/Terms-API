# Generated by Django 3.2.9 on 2021-11-15 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_to_text',
            name='image',
            field=models.ImageField(upload_to='text_extract'),
        ),
    ]
