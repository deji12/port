from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=1000)
    email = models.EmailField()
    message = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class port(models.Model):
    file = models.FileField(upload_to='media')