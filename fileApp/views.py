from django.shortcuts import render
from .forms import ImageForm
from django.contrib import messages
from .models import Image

# Create your views here.

def index(req):
    form = ImageForm()
    if req.method == "POST":
        form = ImageForm(req.POST, req.FILES)
        if form.is_valid():
            img_obj = form.save()
            messages.success(req, 'Logo has been uploaded.')
            return render(req, 'index.html', {'form': form, 'img_obj':img_obj})

    else:
        form = ImageForm()
        return render(req, 'index.html', {'form':form})