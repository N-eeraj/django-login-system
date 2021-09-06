from django.db import models

# Create your models here.
class LoginTable(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    mail = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)   