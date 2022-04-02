from django.shortcuts import render,redirect, get_object_or_404
from django.http  import HttpResponse
from .models import Image,Profile,NewsLetterRecipients,Comment,User,Follow
from .forms import NewsLetterForm, NewArticleForm
from django.contrib.auth.decorators import login_required
from .forms import UploadForm,ProfileForm,UpdateUserForm,UpdateUserProfileForm,CommentForm
from django.db.models.signals import post_save
from django.urls import reverse_lazy,reverse


# Create your views here.
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import send_welcome_email

@login_required(login_url='/accounts/login/')
def home(request):
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

            HttpResponseRedirect('home')
    else:
        form = NewsLetterForm()
    return render(request, 'home.html',{'profile':profile,'image':image,"letterForm":form})
def get_context_data(request,*args, **kwargs):
    context = super(home).get_context_data(request,*args,)
    stuff = get_object_or_404(Image,id=kwargs['pk'])
    total_likes = stuff.total_likes()
    context['total_likes'] = total_likes
    return context

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
        return redirect('home')

    else:
        form = NewArticleForm()
    return render(request, 'new_image.html', {"form": form})

def get_user_profile(request, profile):
    user = Profile.objects.get(profile=profile)
    return render(request, 'user_profile.html', {"user":user})

@login_required(login_url='/accounts/login/')
def profile(request):
    images = request.user.profile.images.all()
    print(images)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        'images': images,
    }
    return render(request, 'profile.html', params)
@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('profile')
    else:
        form = UploadForm()
    return render(request,'edit_profile.html',{"form":form})
@login_required(login_url='/accounts/login/')
def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    user_posts = user_prof.profile.images.all()
    
    followers = Follow.objects.filter(followed=user_prof.profile)
    follow_status = None
    for follower in followers:
        if request.user.profile == follower.follower:
            follow_status = True
        else:
            follow_status = False
    params = {
        'user_prof': user_prof,
        'user_posts': user_posts,
        'followers': followers,
        'follow_status': follow_status
    }
    return render(request, 'user_profile.html', params)
def like( request,pk):
    image = get_object_or_404(image, id=request.POST.get('image_id'))
    image.likes.add(request.user)
    return HttpResponseRedirect(reverse('home', args=[str(pk)]))