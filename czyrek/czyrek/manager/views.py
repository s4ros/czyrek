####################
## Python imports
import hashlib
####################
## Django imports
from django.shortcuts import render
from django.shortcuts import redirect
####################
## forms
from .forms import AddUserPostForm
from .forms import LoginForm
####################
## models
from django.contrib.auth.models import User

####################
## functions
def generateSHA1(text):
    sha_1 = hashlib.sha1()
    sha_1.update(text.encode("utf-8"))
    return sha_1.hexdigest()

####################
## views
def list_users(request):
    all_users = User.objects.order_by('username')
    context = { 'all_users' : all_users }
    return render(request, "list_users.html", context)

# add_user
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


# index after login
def index_after_login(request):
    context = {}
    return render(request, "index.html", context)


# list_candidates
def list_candidates(request):
    context = {}
    return render(request, "list_candidates.html", context)

# list_schools
def list_schools(request):
    context = {}
    return render(request, "list_schools.html", context)

# list_languages
def list_languages(request):
    context = {}
    return render(request, "list_languages.html", context)

# list_profiles
def list_profiles(request):
    context = {}
    return render(request, "list_profiles.html", context)

# list_subjects
def list_subjects(request):
    context = {}
    return render(request, "list_subjects.html", context)

# index_login
def index_login(request):
    if request.method == 'POST':
        return redirect('list_users')
    else:
        form = LoginForm()
        context = {'form' : form}
        return render(request, 'index_login.html', context)


# delete_user
def delete_user(request, user_id):
    User.objects.filter(id=user_id).delete()
    return redirect('list_users')
