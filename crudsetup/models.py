from django.db import models

# Create your models here.
class Booklist(models.Model):
  title=models.CharField(max_length=300,default="")
  price=models.IntegerField(default="0")
  author=models.CharField(max_length=300,default="")

  def __str__(self):
      return self.title
  

