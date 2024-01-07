from django.db import models

# Create your models here.
class Topics(models.Model):
    Topics=models.CharField(max_length=255,primary_key=True)
    def __str__(self):
        return self.Topics


class Webpage(models.Model):
    Topics=models.ForeignKey(Topics,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    urls=models.URLField()

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    Author=models.CharField(max_length=255)

    def __str__(self):
        return self.Author
