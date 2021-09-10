from django import forms
from .models import Movie, edu
from .models import Sports
from .models import Image2
from .models import controversy
from .models import actor
class ImageForm(forms.ModelForm):
 class Meta:
  model = Movie
  fields = '__all__'
  labels = {'photo':''}
class ImageForm1(forms.ModelForm):
 class Meta:
  model = Sports
  fields = '__all__'
  labels = {'photo':''}
class ImageForm2(forms.ModelForm):
 class Meta:
  model = Image2
  fields='__all__'
labels={'photo':''}
class ImageForm3(forms.ModelForm):
  class Meta:
    model=controversy
    fields='__all__'
    labels={'photo':''}
class ImageForm4(forms.ModelForm):
  class Meta:
    model=actor
    fields='__all__'
    labels={'photo':''}
class ImageForm5(forms.ModelForm):
  class Meta:
    model=edu
    fields='__all__'
    labels={'photo':''}