from django.shortcuts import render,redirect
from.models import Ourprojects,About
# Create your views here.
def index(request):
    return redirect('/')

def projects(request):

    ourprojects = Ourprojects.objects.all()

    return render(request,'projects.html',{'ourprojects':ourprojects})

def about(request):

    abouts = About.objects.all()

    return render(request,'about.html',{'abouts':abouts})


def contact(request):

    return render(request,'contact.html')