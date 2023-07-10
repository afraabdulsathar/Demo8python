from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Profile
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    ob=Profile.objects.all()
    return render(request,"index.html",{'result':obj,'ans':ob})
