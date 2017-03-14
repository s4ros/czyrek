####################
## Python imports

####################
## Django imports
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
####################
## forms
from .forms import AddUserPostForm
from .forms import LoginForm
####################
## models
from django.contrib.auth.models import User

####################
## views
@login_required(login_url='/')
def list_users(request):
    all_users = User.objects.order_by('id')
    users_count = all_users.count()
    # to trzeba bedzie zmienic na permissiony... jak juz beda zaimplementowane
    is_admin = request.user.is_staff
    context = { 'all_users' : all_users,
               'users_count' : users_count,
               'is_admin' : is_admin }
    return render(request, "list_users.html", context)

####################
# add_user
@login_required(login_url='/')
def add_user(request):
    if request.method == 'POST':
        print(repr(request))
        form = AddUserPostForm(request.POST)
        if form.is_valid:
            new_user = form.save(commit=False)
            new_user.username = request.POST['username']
            new_user.email = request.POST['email']
            new_user.set_password(request.POST['password'])
            new_user.first_name = request.POST['first_name']
            new_user.last_name = request.POST['last_name']
            if 'is_staff' in request.POST:
                new_user.is_staff = True
            # new_user.permissions = request.POST['permissions']
            new_user.save()
            return redirect('list_users')
    else:
        form = AddUserPostForm()
        context = {'form' : form}
        return render(request, "add_user.html", context)

####################
# index after login
@login_required(login_url='/')
def index_after_login(request):
    return render(request, "index.html")

####################
# list_candidates
@login_required(login_url='/')
def list_candidates(request):
    context = {}
    return render(request, "list_candidates.html", context)

####################
# list_schools
@login_required(login_url='/')
def list_schools(request):
    context = {}
    return render(request, "list_schools.html", context)

####################
# list_languages
@login_required(login_url='/')
def list_languages(request):
    context = {}
    return render(request, "list_languages.html", context)

####################
# list_profiles
@login_required(login_url='/')
def list_profiles(request):
    context = {}
    return render(request, "list_profiles.html", context)

####################
# list_subjects
@login_required(login_url='/')
def list_subjects(request):
    context = {}
    return render(request, "list_subjects.html", context)

####################
# index_login
def index_login(request):
    username = password = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return redirect('index_login')
    else:
        form = LoginForm()
        context = {'form' : form}
        return render(request, 'index_login.html', context)

####################
# user logout
@login_required(login_url='/')
def logout_user(request):
    logout(request)
    context = { 'action': 'logout' }
    return redirect('index_login')

####################
# delete_user
@login_required(login_url='/')
def delete_user(request, user_id):
    User.objects.filter(id=user_id).delete()
    return redirect('list_users')
