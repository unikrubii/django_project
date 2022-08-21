from django.db import models

# Create your models here.
class User(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)