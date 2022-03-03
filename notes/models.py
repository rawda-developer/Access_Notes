from django.db import models
from django.contrib.auth.models import User
class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    def __str__(self):
        return f"Note #{self.id}: {self.title}"