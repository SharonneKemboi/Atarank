from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponse,HttpResponseRedirect,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile,Project,Review
from .forms import MyProjectForm,UpdateProfileForm,ProfileForm
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnly
from atawards import serializer
from .serializer import ProfileSerializer,ProjectSerializer
from rest_framework.response import Response


# Create your views here.
@login_required(login_url='/accounts/login/')
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
                return redirect('profile') 

    mfm = {"form":form}
    return render(request, 'update_profile.html', mfm)    



@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    title = "Add Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'add_profile.html', {"form": form, "title": title})


@login_required(login_url='/accounts/login/')
def search_project(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        images = Project.search_project_name(search_term)
        message = f'{search_term}'

        return render(request, 'search_result.html', {'found': message, 'images': images})
    else:
        message = 'Not found'
        return render(request, 'search_result.html', {'danger': message})



def project_details(request, project_id):
    project = Project.objects.get(id=project_id)
    reviews = Review.objects.filter(project = project)

    return render(request, "project_details.html", {"project": project,"reviews":reviews})    



@login_required(login_url='/accounts/login/')
def review_project(request,id):
    if request.method == 'POST':
        project = Project.objects.get(id=id)
        current_user = request.user

        design_review = request.POST['design']
        content_review = request.POST['content']
        usability_review = request.POST['usability']


        Review.objects.create(
            project=project,
            user=current_user,
            design_review=design_review,
            usability_review=usability_review,
            content_review=content_review,
            avg_review=round((float(design_review)+float(usability_review)+float(content_review))/3,2),
        )

        
        return render(request,'project_details.html',{"project":project})

    else:
        project = Project.objects.get(id=id)

        return render(request,'project_details.html',{"project":project})





class ProjectList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self,request,format=None):
        projects = Project.objects.all()
        serializer =ProjectSerializer(projects,many=True)
        return Response(serializer.data)

        

class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self,request,format=None):
        profiles = Profile.objects.all()
        serializer =ProfileSerializer(profiles,many=True)
        return Response(serializer.data)        