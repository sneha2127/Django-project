from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from .forms import SignUpForm, LoginForm, BlogPost
from django.contrib import messages
from django.contrib.auth.models import User,Group
from .models import Post
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# Home View
def home(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def dashboard(request):
    obj = request.user
    try:
        user = User.objects.get(username=obj)
    except User.DoesNotExist:
        user = None
    if user is not None:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'blog/dashboard.html',{'posts':posts,'full_name':full_name,'groups':gps})
    else:
        messages.error(request,'Please enter a valid username or password. Note that both the fields are case-sensitive.')
        return HttpResponseRedirect('/userlogin/')

def user_login(request):
    print("request.user",request.user)
    if True:
        if request.method == 'GET':
            form = LoginForm()

        elif request.method== 'POST':
            # data = request.POST or request.GET
            uname = request.POST.get('username')
            upass = request.POST.get('password')
            try:
                user = User.objects.get(username=uname, password=upass)
            except:
                user = None
                form = LoginForm()
                messages.error(request, 'Please Enter a Valid user and password.  Note that both the fields are case-sensitive')
                
            
            print(user)
            if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Succesfully!')
                    return HttpResponseRedirect('/dashboard/',messages)
                
        else:
            print("user not authenticated")
            form = LoginForm()
        return render(request, 'blog/login.html', {'form': form})
        # return HttpResponseRedirect('/signup/'


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User(username=data['username'],first_name=data['first_name'],last_name=data['last_name'],email=data['email'],
                           password=data['password1']) 
            user.save()
            form = SignUpForm()
            messages.success(request, "Congratulations! You are an authour now!")
            group = Group.objects.get(name='Author')
            user.groups.add(group)

    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html',{'form': form})


# Add New Post
def user_add_post(request):
    form = BlogPost()
    obj = request.user
    try:
        user = User.objects.get(username=obj)
    except User.DoesNotExist:
        user = None
    if user is not None:
        if request.method == 'POST':
            form = BlogPost(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                db_data = Post(title=data['title'], description=data['description'])
                db_data.save()
                form = BlogPost()
                messages.success(request,'Your Post has been added Successfully!')
                return HttpResponseRedirect('/dashboard/')
        else:
            form = BlogPost()
            user = request.user
            full_name = user.get_full_name()
            gps = user.groups.all
            return render(request, 'blog/addPost.html', {'form': form,'full_name':full_name,'groups':gps})
    else:
        print("user not authenticated")
        return HttpResponseRedirect('/userlogin/')
       
    
# Update Existing Post
def user_update_post(request,id = id):
    obj = request.user
    try:
        user = User.objects.get(username=obj)
    except User.DoesNotExist:
        user = None
    if user is not None:
        post = Post.objects.get(pk= id)
        if request.method == 'POST':
            form = BlogPost(request.POST, instance= post)
            if form.is_valid():
                data = form.cleaned_data
                post.title = data['title']
                post.description = data['description']
                post.save()
                messages.success(request,'Your Post has been updated Successfully!')
                return HttpResponseRedirect('/dashboard/')
        else:
            form= BlogPost(instance=post)
            return render(request, 'blog/updatepost.html', {'form': form, 'id':id})
    else:
        print("user not authenticated")
        return HttpResponseRedirect('/userlogin/')


# Delete Existing post
def user_delete_post(request, id=id):
    obj = request.user
    try:
        user = User.objects.get(username=obj)
    except User.DoesNotExist:
        user = None
    if user is not None:
        if request.method == 'POST':
            post = Post.objects.get(id=id)
            title = post.title
            post.delete()
            messages.success(request,f'Post named "{title}" has been deleted')
        
    else:
        messages.error(request, 'Error deleting the post.')
        return HttpResponseRedirect('/userlogin/')

    return HttpResponseRedirect('/dashboard/')
