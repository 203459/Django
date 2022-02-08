from django.db import models
from django.utils import timezone

# Create your models here.
class TablaImage(models.Model):
    name_img = models.CharField(max_length=50, null=True)
    url_img = models.ImageField(blank='', default="", upload_to='assets/img/')
    format_img = models.CharField(max_length=50, null=True)
    created = models.DateTimeField(default=timezone.now)
    editted = models.DateTimeField(blank=True, null=True, default=None)

 