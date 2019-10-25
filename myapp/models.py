from django.db import models

# Create your models here.
class Topic(models.Model):
    topic=models.CharField(primary_key=True,max_length=20)

    def __str__(self):
        return self.topic

class Webpage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(primary_key=True,max_length=50)
    url=models.CharField(unique=True,max_length=50)
    def __str__(self):
        return self.name

class Access_Records(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return str(self.date)







