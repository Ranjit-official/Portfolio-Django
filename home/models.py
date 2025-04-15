from django.db import models

# Create your models here.
class Certification(models.Model):
    name = models.CharField(max_length=200,blank=False)
    slug = models.CharField(unique=True,max_length=100,blank=False)
    image = models.ImageField(upload_to="media/certification")

    def __str__(self):
        return self.name
    
class Experience(models.Model):
    name = models.CharField(max_length=200,blank=False)
    post = models.CharField(max_length=100,blank=False)
    startDate = models.CharField(max_length=50)
    endDate = models.CharField(max_length=50)
    image =models.ImageField(upload_to='media/experience')
    slug = models.CharField(max_length=200,unique=True,blank=False)

    def __str__(self):
        return f"{self.name} + {self.post}"

class TechnicalSkills(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=100,unique=True,blank=False)

    def __str__(self):
        return self.name
    