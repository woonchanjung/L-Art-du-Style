import os
import uuid
import boto3
import imghdr
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import TopForm, BottomForm
from .models import Top, Bottom, Match
from django.contrib import messages
# Create your views here.

# Define the home view


def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def index(request):
    tops = Top.objects.filter(user=request.user)
    bottoms = Bottom.objects.filter(user=request.user)
    return render(request, 'clothes/index.html', {'tops': tops, 'bottoms': bottoms})


@login_required
def upload_top(request):
    if request.method == 'POST':
        form = TopForm(request.POST, request.FILES)
        if form.is_valid():
            photo_files = request.FILES.getlist('image')
            if len(photo_files) > 0:
                for photo_file in photo_files:
                    if photo_file:
                        if imghdr.what(photo_file) is not None:
                            s3 = boto3.client('s3')
                            key = f"tops/{uuid.uuid4().hex[:6]}{os.path.splitext(photo_file.name)[1]}"
                            try:
                                bucket = os.environ['S3_BUCKET']
                                s3.upload_fileobj(photo_file, bucket, key)
                                url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
                                new_top = Top(user=request.user, image=url)
                                new_top.save()
                            except Exception as e:
                                print('An error occurred uploading file to S3')
                                print(e)
                        else:
                            form.add_error(
                                'image', 'Please select an image file.')
                return redirect('index')
            else:
                form.add_error('image', 'Please select at least one file.')
    else:
        form = TopForm()
    return render(request, 'clothes/upload_top.html', {'form': form})


@login_required
def upload_bottom(request):
    if request.method == 'POST':
        form = BottomForm(request.POST, request.FILES)
        if form.is_valid():
            photo_files = request.FILES.getlist('image')
            if len(photo_files) > 0:
                for photo_file in photo_files:
                    if photo_file:
                        if imghdr.what(photo_file) is not None:
                            s3 = boto3.client('s3')
                            key = f"bottoms/{uuid.uuid4().hex[:6]}{os.path.splitext(photo_file.name)[1]}"
                            try:
                                bucket = os.environ['S3_BUCKET']
                                s3.upload_fileobj(photo_file, bucket, key)
                                url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
                                new_bottom = Bottom(
                                    user=request.user, image=url)
                                new_bottom.save()
                            except Exception as e:
                                print('An error occurred uploading file to S3')
                                print(e)
                        else:
                            form.add_error(
                                'image', 'Please select an image file.')
                return redirect('index')
            else:
                form.add_error('image', 'Please select at least one file.')
    else:
        form = BottomForm()
    return render(request, 'clothes/upload_bottom.html', {'form': form})


@login_required
def create_match(request):
    if request.method == 'POST':
        top_id = request.POST.get('top')
        bottom_id = request.POST.get('bottom')
        
        if top_id and bottom_id:
            top = get_object_or_404(Top, id=top_id, user=request.user)
            bottom = get_object_or_404(Bottom, id=bottom_id, user=request.user)
            # Perform any additional processing or save the match to the database
            messages.success(request, 'Match created successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Please select a top and a bottom.')
    
    tops = Top.objects.filter(user=request.user)
    bottoms = Bottom.objects.filter(user=request.user)
    return render(request, 'clothes/create_match.html', {'tops': tops, 'bottoms': bottoms})

@login_required
def view_matches(request, message=None):
    matches = Match.objects.filter(user=request.user)
    return render(request, 'clothes/view_matches.html', {'matches': matches, 'message': message})


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


@login_required
def delete_top(request, top_id):
    top = get_object_or_404(Top, id=top_id)
    if request.user == top.user:
        # Delete the image from S3
        s3 = boto3.client('s3')
        key = top.image.url.split('/')[-1]
        bucket = os.environ['S3_BUCKET']
        try:
            s3.delete_object(Bucket=bucket, Key=key)
        except Exception as e:
            print('An error occurred deleting file from S3')
            print(e)
        top.delete()
    return redirect('index')


@login_required
def delete_bottom(request, bottom_id):
    bottom = get_object_or_404(Bottom, id=bottom_id)
    if request.user == bottom.user:
        # Delete the image from S3
        s3 = boto3.client('s3')
        key = bottom.image.url.split('/')[-1]
        bucket = os.environ['S3_BUCKET']
        try:
            s3.delete_object(Bucket=bucket, Key=key)
        except Exception as e:
            print('An error occurred deleting file from S3')
            print(e)
        bottom.delete()
    return redirect('index')


@login_required
def delete_match(request, match_id):
    if request.method == 'POST':
        match = Match.objects.get(pk=match_id)
        match.delete()
        return redirect('view_matches')


@login_required
def edit_top(request, top_id):
    top = get_object_or_404(Top, id=top_id, user=request.user)
    if request.method == 'POST':
        form = TopForm(request.POST, request.FILES, instance=top)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TopForm(instance=top)
    return render(request, 'clothes/edit_top.html', {'form': form, 'top': top})


@login_required
def edit_bottom(request, bottom_id):
    bottom = get_object_or_404(Bottom, id=bottom_id, user=request.user)
    if request.method == 'POST':
        form = BottomForm(request.POST, instance=bottom)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BottomForm(instance=bottom)
    return render(request, 'clothes/edit_bottom.html', {'form': form, 'bottom': bottom})

