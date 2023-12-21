from django.db import models



class CrudItem(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
