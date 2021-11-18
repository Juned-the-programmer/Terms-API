from django.db import models

# Create your models here.
class Image_to_Text(models.Model):
    image = models.ImageField(upload_to="static/text_extract")