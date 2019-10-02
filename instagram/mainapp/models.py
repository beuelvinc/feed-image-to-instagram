from django.db import models

# Create your models here.
class Instagram(models.Model):
    username=models.CharField(max_length=50)
    password =models.CharField(max_length=50)
    image=models.ImageField(upload_to="insta")
    date=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=["-date"]