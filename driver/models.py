from django.db import models


class Driver(models.Model):
    name = models.CharField(max_length=250, null=True)
    email = models.EmailField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)


