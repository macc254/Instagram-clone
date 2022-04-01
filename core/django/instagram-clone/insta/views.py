from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image,Profile


# Create your views here.
def profile(request):
    profile = Profile.objects.all()

    return render(request, 'home.html',{'profile':profile})

def display_image(request):
    image = Image.objects.all()
    return render(request,'all-images.html',{'image':image})

