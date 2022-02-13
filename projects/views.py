from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from projects.utils import searchProject
from .models import Project, Review
from .forms import commentform, projectform

def projects(request):
    

    projects, search_query= searchProject(request)

    return render(request,'projects.html',{'projects': projects, 'search_query': search_query})



def project(request, pk):
    form= commentform()
    project_obj= Project.objects.get(id= pk)


    if request.method== 'POST':
        form= commentform(request.POST)
        if form.is_valid():
            review= form.save(commit= False)
            review.owner= request.user.profile
            review.project= project_obj
            review.save()
            return redirect('project', pk=project_obj.id )



    return render(request,'project.html',{'project': project_obj , 'commentform': form})


@login_required(login_url='loginUser')
def create_project(request):
    profile = request.user.profile
    form= projectform()
    
    if request.method== 'POST':
        form= projectform(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')
    
    return render(request,'create_project.html',{'form': form})


@login_required(login_url='loginUser')
def update_project(request, pk):
    project= Project.objects.get(id= pk)

    form= projectform(instance= project)

    if request.method== 'POST':
        form= projectform(request.POST, request.FILES , instance= project)
        if form.is_valid():
            form.save()
            return redirect('projects')
            
    
    return render(request,'create_project.html',{'form': form})


@login_required(login_url='loginUser')
def delete_project(request, pk):
    project= Project.objects.get(id= pk)


    if request.method== 'POST':
        project.delete()
        messages.warning(request, 'Project was deleted!')
        return redirect('projects')
    
    return render(request,'delete_project.html',{'project': project})