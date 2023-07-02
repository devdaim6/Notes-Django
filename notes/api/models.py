from django.db import models


# Create your models here.


class Note(models.Model):
    body=models.TextField(null=True,blank=True)
    updated=models.DateTimeField(auto_now=True) #whenever updated timestamp is updated
    created=models.DateTimeField(auto_now_add=True) #only takes timestamp on creation of models
    
    def __str__(self) -> str:
        return self.body[0:20]
    
    
 