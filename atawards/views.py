from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile,Project
from .forms import MyProjectForm,UpdateProfileForm


# Create your views here.

def index(request):

    myproj =Project.objects.all().order_by('-id')

    return render(request, 'all-atawards/index.html',{'myproj':myproj})
   

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    project = Project.objects.filter(user_id=current_user.id)

    return render(request,"profile.html",{'profile':profile ,'project':project})


@login_required(login_url='/accounts/login/')
def upload(request):
    if request.method == 'POST':
        form=MyProjectForm(request.POST,request.FILES)
        if form.is_valid():
            myproj =form.save(commit=False)
            myproj.save()
            return redirect('/')
        else:
            form=MyProjectForm()
        return render(request,"my_project.html",{'form':form})          



@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  

                profile = form.save(commit=False)
                profile.save()
                return redirect('profile' ,username=user.username) 

    ctx = {"form":form}
    return render(request, 'update_profile.html', ctx)    