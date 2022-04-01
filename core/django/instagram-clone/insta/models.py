from django.db import models
class Image(models.Model):
    image = models.ImageField(upload_to='images/',default='1')
    name = models.CharField(max_length =30)
    caption = models.CharField(max_length =30)
    profile = models.ForeignKey('Profile',on_delete=models.CASCADE,default='0')
    likes = models.IntegerField()
    comments = models.CharField(max_length =30)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
        
    def save_image(self):
        self.save()
        
        
class Profile(models.Model):
    bio = models.CharField(max_length =30)
    profile_photo = models.ImageField(upload_to ='images/',default='1')

    def __str__(self):
        return self.bio
