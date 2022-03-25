from unicodedata import category
from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50,null=True)
    slug=models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name


# Create your models here.
class Course(models.Model):
    category=models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=200,unique=True,verbose_name="Kurs Adı",help_text="Kurs adını yazınız")
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to="courses/&Y/%m/%d/",default="courses/default_course_image.jpg")
    date=models.DateField(auto_now=True)
    available=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
