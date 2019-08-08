from django.db import models

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(null= True, blank=True)
    email = models.EmailField(blank=True,null=True)



    def __str__(self):
        return self.title


