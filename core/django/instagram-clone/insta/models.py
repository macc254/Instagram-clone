from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length =30)
    caption = models.CharField(max_length =30)
    profile = models.ForeignKey( 'Profile', on_delete=models.CASCADE,default=1)


    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
class Profile(models.Model):
    bio = models.CharField(max_length =30)

    def __str__(self):
        return self.bio
