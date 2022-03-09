from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Entry(models.Model):
    preview = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='entry')
    title = models.CharField(max_length=100)
    text = models.TextField()
    last_edit_date = models.DateTimeField()
    depression = models.BooleanField(default=False)

    class Meta:
        ordering = ['-last_edit_date']

    def __str__(self):
        return self.title


class CheckIn(models.Model):
    score = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='checkin')
    date = models.DateField()

    def __str__(self):
        return f"{self.user} - {self.date}"


