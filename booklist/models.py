from django.db import models

class BookList(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.URLField(max_length = 200)

    def __str__(self):
        return self.name