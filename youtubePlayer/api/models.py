from django.db import models


class History(models.Model):
    url = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True, blank=True)



