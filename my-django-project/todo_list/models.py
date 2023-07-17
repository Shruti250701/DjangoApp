from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone

class TaskList(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()     
    is_completed= models.BooleanField(default=False)

    def publish(self):
        self.start_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['is_completed', 'start_date']