from django.db import models
from author.models import author
# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=250)
   #auther
    published_at=models.DateTimeField()
    add_to_site=models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    appropriate=models.CharField(max_length=250,choices=[("8","Kid"),("8-15","teenager"),("15+","adult")],default="adult")
    author=models.ForeignKey(author,on_delete=models.CASCADE,null=True)
    image = models.ImageField (max_length=255, upload_to="img/%y",null=True)

    def __str__(self):
        return self.name
