import os
import uuid
import boto3
import logging
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from .models import Clothes, ClothingItem

# Create your views here.

# Define the home view


def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def clothes_index(request):
    clothes = Clothes.objects.filter(user=request.user)
    # You could also retrieve the logged in user's cats like this
    # cats = request.user.cat_set.all()
    return render(request, 'clothes/index.html', {
        'clothes': clothes
    })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def upload_photo(request, clothe_id):
    if request.method == 'POST':
        clothe = ClothingItem.objects.get(pk=clothe_id)
        top_photo = request.FILES['top_photo']
        bottom_photo = request.FILES['bottom_photo']

        # Upload top photo to S3
        s3 = boto3.client('s3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME
        )
        top_photo_key = f'top/{clothe.id}.jpg'
        s3.upload_fileobj(top_photo, settings.AWS_STORAGE_BUCKET_NAME, top_photo_key)

        # Upload bottom photo to S3
        bottom_photo_key = f'bottom/{clothe.id}.jpg'
        s3.upload_fileobj(bottom_photo, settings.AWS_STORAGE_BUCKET_NAME, bottom_photo_key)

        # Update the clothe's photo URLs
        clothe.top_photo_url = f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/{top_photo_key}'
        clothe.bottom_photo_url = f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/{bottom_photo_key}'
        clothe.save()

        return redirect('clothe_detail', clothe_id=clothe.id)

    clothe = ClothingItem.objects.get(pk=clothe_id)
    context = {'clothe': clothe}
    return render(request, 'myapp/upload_photo.html', context)