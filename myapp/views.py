from django.shortcuts import render
from .forms import ImageForm,ImageForm1,ImageForm2,ImageForm3,ImageForm4,ImageForm5
from .models import Movie,Sports,Image2, actor,controversy,edu
# Create your views here.

def home(request):
 return render(request, 'myapp/home.html')
def index(request):
 if request.method == "POST":
  form = ImageForm(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm()
 img = Movie.objects.all()
 return render(request, 'myapp/index.html', {'img':img, 'form':form})
def sports(request):
 if request.method == "POST":
  form = ImageForm1(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm1()
 img = Sports.objects.all()
 return render(request, 'myapp/sports.html', {'img':img, 'form':form})
def technology(request):
 if request.method == "POST":
  form = ImageForm2(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm2()
 img = Image2.objects.all()
 return render(request, 'myapp/technology.html', {'img':img, 'form':form})
def Controversy(request):
 if request.method == "POST":
  form = ImageForm3(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm3()
 img = controversy.objects.all()
 return render(request, 'myapp/Controversy.html', {'img':img, 'form':form})
def Actor(request):
 if request.method == "POST":
  form = ImageForm4(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm4()
 img = actor.objects.all()
 return render(request, 'myapp/Actor.html', {'img':img, 'form':form})
def education(request):
 if request.method == "POST":
  form = ImageForm5(request.POST, request.FILES)
  if form.is_valid():
   form.save()
 form = ImageForm5()
 img = edu.objects.all()
 return render(request, 'myapp/education.html', {'img':img, 'form':form})
