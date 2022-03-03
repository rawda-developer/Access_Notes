from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)

    def __str__(self):
        return f"Note #{self.id}: {self.title}"