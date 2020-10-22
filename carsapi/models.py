from django.db import models

class car(models.Model):
    make = models.CharField(max_length=60)

    def __str__(self):
        return self.name
