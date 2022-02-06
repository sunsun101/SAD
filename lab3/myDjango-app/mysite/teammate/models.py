from django.db import models

class Teammate(models.Model):
    title = models.CharField(max_length=10, default="Mr.")
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id} {self.title} {self.first_name} {self.last_name}"
