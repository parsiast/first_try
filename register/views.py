from django.http import HttpResponse
from django.shortcuts import render 
from django.utils import timezone
from .models import Usersinfo

def register_user(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Usersinfo.objects.filter(username=username).exists():
            return HttpResponse(f"username {username} already exists. Please choose a different username.")
    
        user = Usersinfo(username=username, password=password ,published=timezone.now())
        user.save()
        return HttpResponse(f"User {username} created successfully!")
    return render(request, "blog/index.html")

    
    
def user_detail(request,user_id):
    user_instance= Usersinfo.objects.get(id=user_id)
    response_text=f"username{user_id}={user_instance.username} & pubdate{user_id}={user_instance.published.date()}"
    return HttpResponse (response_text)

def firstp (request):
    return HttpResponse("hi this a site for register some users and control them ")