from django.db import models
from django.urls import reverse

class Page(models.Model):
    title = models.CharField(max_length=64, primary_key=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
    #    return reverse('wiki:detail', args=[self.title])

class UserFileUpload(models.Model):
    upload = models.FileField(upload_to='uploads/')
    #file will be saved to MEDIA_ROOT/uploads

    def __str__(self):
        return self.upload.name