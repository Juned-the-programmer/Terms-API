# Generated by Django 3.2.9 on 2021-11-15 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_alter_image_to_text_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_to_text',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
