from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image,Profile


# Create your views here.
def welcome(request):
    return render(request, 'home.html')

def display_image(request):
    profile = Profile.objects.all()
    image = Image.objects.all()
    return render(request,'all-images.html',{'image':image,'profile':profile})

