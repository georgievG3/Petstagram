from django.db import models

from photos.models import Photo


# Create your models here.
class Comment(models.Model):
    class Meta:
        ordering = ['-date_time_of_publication']

    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo  = models.ForeignKey(Photo, on_delete=models.CASCADE)

class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
