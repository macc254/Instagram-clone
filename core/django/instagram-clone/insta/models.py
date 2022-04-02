from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    image = models.ImageField(upload_to='images/',default='1')
    name = models.CharField(max_length =30)
    caption = models.CharField(max_length =30)
    profile = models.ForeignKey(User,on_delete=models.CASCADE,default='0')
    likes = models.IntegerField()
    comments = models.CharField(max_length =30)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
        
    def save_image(self):
        self.save()
    @classmethod
    def search_by_name(cls, image):
        images = cls.objects.filter(image__icontains=image)
        return images
        
class Profile(models.Model):
    bio = models.CharField(max_length =30)
    profile_photo = models.ImageField(upload_to ='images/',default='1')
    name = models.CharField(blank=True, max_length=120)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)



    def __str__(self):
        return self.bio
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

# likes = models.ManyToManyField(User,related_name=)