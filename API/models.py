from django.db import models

# Create your models here.
class Image_to_Text(models.Model):
    name = models.CharField(max_length=100 , blank=True , null=True)
    image = models.ImageField(upload_to="text_extract")

    def __str__(self):
        return self.name