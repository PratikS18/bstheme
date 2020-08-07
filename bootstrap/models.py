from django.db import models

# Create your models here.

LINK_TYPES = (
    ("Website","Website"),
    ("Filehoster","Filehoster"),
    ("Torrent","Torrent"),
)

class TopList(models.Model):
    ISBN = models.CharField(max_length = 20, blank = False)
    Book_name = models.CharField(max_length = 150)

    def __str__(self):
        return self.Book_name

class RawData(models.Model):
    ISBN = models.CharField(max_length = 20, blank = False)
    link = models.CharField(max_length=150)
    date_found = models.DateField(null=True, blank=True)
    date_resolved = models.DateField(null=True, blank=True)
    link_type = models.CharField(max_length = 20, choices=LINK_TYPES, blank = False, default='Website')

    def __str__(self):
        return self.link
