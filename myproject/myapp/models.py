from django.db import models

# Create your models here.
class Items(models.Model):
    name=models.CharField(max_length=20)
    rate=models.PositiveIntegerField(max_length=20)

    def __Str__(self):
        return self.name
