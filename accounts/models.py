from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    UNI_CHOICES = [
        ("KU", "Kenyatta University"),
        ("JKUAT", "Jomo Kenyatta Univeristy Of Agriculture and Technology"),
        ("TUK", "Technical University of Kenya"),
        ("UON", "University Of Nairobi"),
        ("TUM", "Technical University of Mombasa"),
        ("DeKUT", "Dedan Kimathi University of Technology")
    ]
    university = models.CharField(max_length=100, choices=UNI_CHOICES)

    def __str__(self):
        return self.username
