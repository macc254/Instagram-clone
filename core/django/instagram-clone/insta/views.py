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


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        results = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": results})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

