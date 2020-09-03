from django.contrib import admin
from django.shortcuts import render
# Register your models here.
def homepage(request):
    return render(request, 'index.html', locals())