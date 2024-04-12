from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class upload_audio(models.Model):
    filename = models.FileField(upload_to='audio')
    upload_date = models.DateTimeField(auto_now_add=True)
    upload_by = models.ForeignKey(User, on_delete=models.CASCADE)
    summary_gen = models.BooleanField(default=False)
    transcript_gen = models.BooleanField(default=False)
    mom_gen = models.BooleanField(default=False)

    def __str__(self):
        return str(self.filename.name) + " " + self.upload_by.first_name


class audio_summary(models.Model):
    audio = models.ForeignKey(upload_audio, on_delete=models.CASCADE)
    summary = models.TextField()
    summary_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.audio.filename) + " " + self.audio.upload_by.first_name


class audio_transcript(models.Model):
    audio = models.ForeignKey(upload_audio, on_delete=models.CASCADE)
    transcript = models.TextField()
    summary_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.audio.filename) + " " + self.audio.upload_by.first_name


class audio_mom(models.Model):
    audio = models.ForeignKey(upload_audio, on_delete=models.CASCADE)
    mom = models.TextField()
    summary_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.audio.filename) + " " + self.audio.upload_by.first_name
