from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Imageform
from .models import Image


def image_view(request):
    if request.method == 'POST':
        form = Imageform(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('display_images')
    else:
        form = Imageform()
    return render(request, 'image_form.html', {'form' : form})


def display_images(request):

    if request.method == 'GET':
        if request.GET.get('category'):
            Images = Image.objects.filter(category = request.GET.get('category')).order_by('-created')
            return render(request, 'display_images.html', {'images': Images})
        else:
            Images = Image.objects.all().order_by('-created')
            category = Image.objects.all().values('category').distinct()
            return render(request, 'display_images.html', {'images' : Images, 'category':category})


