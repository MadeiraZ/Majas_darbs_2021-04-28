from django.db import models

# Create your models here.

class AddUser(models.Model):

    username = models.CharField(max_length=125)
    email = models.EmailField(max_length=125)

    def __str__(self):
        return f'{self.username}: {self.email}'
