from django.db import models


# Create your models here.
class upload_audio(models.Model):
    filename = models.FileField(upload_to='audio')
