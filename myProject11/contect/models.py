from django.db import models

class Contect(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name