from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    email = models.EmailField()
    enroll_date = models.DateField()
    department = models.CharField(max_length=200)


    def __str__(self):
        return self.first_name