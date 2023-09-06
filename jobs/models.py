from django.db import models
from django.contrib.auth import get_user_model

from django.urls import reverse

# Create your models here.
class Jobs(models.Model):
    title = models.CharField(max_length=300)
    employer = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    payment = models.PositiveIntegerField(default=20)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("job_detail", args=[str(self.pk)])
    

class Application(models.Model):
    rate = models.PositiveIntegerField()
    job = models.ForeignKey(
        Jobs,
        on_delete=models.CASCADE
    )
    apply = models.TextField()

