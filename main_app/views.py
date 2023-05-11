import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import TopForm, BottomForm
from .models import Top, Bottom, Match
# Create your views here.

# Define the home view


def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def index(request):
    tops = Top.objects.filter(user=request.user)
    bottoms = Bottom.objects.filter(user=request.user)
    return render(request, 'clothes/index.html', {'tops': tops, 'bottoms': bottoms})


def upload_top(request):
    if request.method == 'POST':
        form = TopForm(request.POST, request.FILES)
        if form.is_valid():
            photo_files = request.FILES.getlist('image')
            for photo_file in photo_files:
                if photo_file:
                    s3 = boto3.client('s3')
                    key = uuid.uuid4(
                    ).hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
                    try:
                        bucket = os.environ['S3_BUCKET']
                        s3.upload_fileobj(photo_file, bucket, key)
                        url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
                        form.instance.user = request.user
                        form.instance.image = url
                        form.save()
                    except Exception as e:
                        print('An error occurred uploading file to S3')
                        print(e)
            return redirect('index')
    else:
        form = TopForm()
    return render(request, 'clothes/upload_top.html', {'form': form})


def upload_bottom(request):
    if request.method == 'POST':
        form = BottomForm(request.POST, request.FILES)
        if form.is_valid():
            photo_files = request.FILES.getlist('image')
            for photo_file in photo_files:
                if photo_file:
                    s3 = boto3.client('s3')
                    key = uuid.uuid4(
                    ).hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
                    try:
                        bucket = os.environ['S3_BUCKET']
                        s3.upload_fileobj(photo_file, bucket, key)
                        url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
                        form.instance.user = request.user
                        form.instance.image = url
                        form.save()
                    except Exception as e:
                        print('An error occurred uploading file to S3')
                        print(e)
            return redirect('index')
    else:
        form = BottomForm()
    return render(request, 'clothes/upload_bottom.html', {'form': form})


def create_match(request):
    tops = Top.objects.filter(user=request.user)
    bottoms = Bottom.objects.filter(user=request.user)
    if tops.exists() and bottoms.exists():
        if request.method == 'POST':
            form = MatchForm(request.POST)
            if form.is_valid():
                top_id = form.cleaned_data['top']
                bottom_id = form.cleaned_data['bottom']
                top = Top.objects.get(id=top_id)
                bottom = Bottom.objects.get(id=bottom_id)
                Match.objects.create(top=top, bottom=bottom, user=request.user)
                return redirect('view_matches')
        else:
            form = MatchForm()
        return render(request, 'clothes/create_match.html', {'form': form, 'tops': tops, 'bottoms': bottoms})
    else:
        message = "Please upload at least one top and one bottom to create a match."
        return render(request, 'clothes/create_match.html', {'message': message})


def view_matches(request):
    matches = Match.objects.all()
    return render(request, 'clothes/view_matches.html', {'matches': matches})


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


# def upload_photo(request, clothe_id):
#     if request.method == 'POST':
#         clothe = ClothingItem.objects.get(pk=clothe_id)
#         top_photo = request.FILES['top_photo']
#         bottom_photo = request.FILES['bottom_photo']

#         # Upload top photo to S3
#         s3 = boto3.client('s3',
#                           aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#                           aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
#                           region_name=settings.AWS_S3_REGION_NAME
#                           )
#         top_photo_key = f'top/{clothe.id}.jpg'
#         s3.upload_fileobj(
#             top_photo, settings.AWS_STORAGE_BUCKET_NAME, top_photo_key)

#         # Upload bottom photo to S3
#         bottom_photo_key = f'bottom/{clothe.id}.jpg'
#         s3.upload_fileobj(
#             bottom_photo, settings.AWS_STORAGE_BUCKET_NAME, bottom_photo_key)

#         # Update the clothe's photo URLs
#         clothe.top_photo_url = f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/{top_photo_key}'
#         clothe.bottom_photo_url = f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/{bottom_photo_key}'
#         clothe.save()

#         return redirect('clothe_detail', clothe_id=clothe.id)

#     clothe = ClothingItem.objects.get(pk=clothe_id)
#     context = {'clothe': clothe}
#     return render(request, 'myapp/upload_photo.html', context)
