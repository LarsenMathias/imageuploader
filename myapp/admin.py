from myapp.views import controversy
from django.contrib import admin
from .models import Movie,Sports,Image2,controversy,actor,edu
# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
 list_display = ['id', 'photo', 'date']
@admin.register(Sports)
class SportsAdmin(admin.ModelAdmin):
 list_display = ['id', 'photo', 'date']
@admin.register(Image2)
class Image2Admin(admin.ModelAdmin):
    list_display=['id','photo','date']
@admin.register(controversy)
class controversyAdmin(admin.ModelAdmin):
    list_display=['id','photo','date']
@admin.register(actor)
class actorAdmin(admin.ModelAdmin):
    list_display=['id','photo','date']
@admin.register(edu)
class eduAdmin(admin.ModelAdmin):
    list_display=['id','photo','date']