from django.db import models

# Create your models here.

class User(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Mobile=models.CharField(max_length=10)

    def __str__(self):
        return self.Name

class Task(models.Model):
    Pending="Pending"
    Done="Done"

    Task_Type=[(Pending,"Pending"),(Done,"Done")]

    Detail = models.ForeignKey(User, on_delete=models.CASCADE)
    Task_type = models.CharField(max_length=10, choices=Task_Type)
    Task= models.TextField()

    def __str__(self):
        return self.Detail.Name
    