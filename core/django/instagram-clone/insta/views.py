from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Image,Profile,NewsLetterRecipients
from .forms import NewsLetterForm, NewArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email

@login_required(login_url='/accounts/login/')
def profile(request):
    profile = Profile.objects.all()
    image = Image.objects.all()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('profile')
    else:
        form = NewsLetterForm()
    return render(request, 'home.html',{'profile':profile,'image':image,"letterForm":form})

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
@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.profile = current_user
            article.save()
        return redirect('profile')

    else:
        form = NewArticleForm()
    return render(request, 'new_image.html', {"form": form})

def get_user_profile(request, profile):
    user = Profile.objects.get(profile=profile)
    return render(request, 'user_profile.html', {"user":user})
