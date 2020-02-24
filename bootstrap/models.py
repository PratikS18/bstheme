from django.db import models

# Create your models here.
class TopList(models.Model):
    ISBN = models.CharField(max_length = 20, blank = False)
    Book_name = models.CharField(max_length = 150)

class RawData(models.Model):
    ISBN = models.CharField(max_length = 20, blank = False)
    link = models.CharField(max_length=150)
    date_found = models.DateField(null=True, blank=True)
    date_resolved = models.DateField(null=True, blank=True)
