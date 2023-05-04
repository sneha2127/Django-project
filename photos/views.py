from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib import messages
from .models import Photo,Category
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def gallery(request):
    user = request.user
    try:
        user = User.objects.get(username=user)
    except User.DoesNotExist:
        user = None
    if user is not None:
        category = request.GET.get('category')
        if category == None:
            photos = Photo.objects.all()
        else:
        # filters the photos according to category
            photos = Photo.objects.filter(category__name__contains=category)
        categories = Category.objects.all()
    
        context = {'categories':categories, 'photos': photos}
        return render(request, 'photos/gallery.html',context)
    else:
        messages.error(request,'Please enter a valid username or password. Note that both the fields are case-sensitive.')
        return HttpResponseRedirect('/userlogin/')

def view_photo(request, pk):
    user = request.user
    try:
        user = User.objects.get(username=user)
    except User.DoesNotExist:
        user = None
    if user is not None:
        photo = Photo.objects.get(id=pk)
        context = {'photo': photo}
        return render(request, 'photos/photo.html',context)
    else:
        messages.error(request,'Please enter a valid username or password. Note that both the fields are case-sensitive.')
        return HttpResponseRedirect('/userlogin/')

def addphoto(request):
    user = request.user
    try:
        user = User.objects.get(username=user)
    except User.DoesNotExist:
        user = None
    if user is not None:
        categories = Category.objects.all()
        if request.method == 'POST':
            data = request.POST
            image = request.FILES.get('image')
            if data['category'] != 'none':
                category = Category.objects.get(id=data['category'])
            elif data['category_new'] != "":
                # below line of code checks if it already exists returns the same else creates a new one and returns that
                category, created = Category.objects.get_or_create(name=data['category_new'])
            else:
                category = None
            photo = Photo.objects.create(
                category=category,
                description = data['description'],
                image = image
            )
            return redirect('gallery')

        context = {'categories':categories}
        return render(request, 'photos/add.html',context)
    else:
        messages.error(request,'Please enter a valid username or password. Note that both the fields are case-sensitive.')
        return HttpResponseRedirect('/userlogin/')