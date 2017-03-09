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
from .models import User

####################
## functions
def generateSHA1(text):
    sha_1 = hashlib.sha1()
    sha_1.update(text.encode("utf-8"))
    return sha_1.hexdigest()

####################
## views
def list_users(request):
    all_users = User.objects.order_by('login')
    context = { 'all_users' : all_users }
    return render(request, "list_users.html", context)

# add_user
def add_user(request):
    if request.method == 'POST':
        print(repr(request))
        form = AddUserPostForm(request.POST)
        if form.is_valid:
            new_user = form.save(commit=False)
            new_user.login = request.POST['login']
            new_user.passwd = str(generateSHA1(request.POST['passwd']))
            new_user.email = request.POST['email']
            new_user.full_name = request.POST['full_name']
            new_user.permissions = request.POST['permissions']
            new_user.save()
            return redirect('list_users')
    else:
        form = AddUserPostForm()
        context = {'form' : form}
        return render(request, "add_user.html", context)


# index_login
def index_login(request):
    if request.method == 'POST':
        return redirect('list_users')
    else:
        form = LoginForm()
        context = {'username': 's4ros', 'form' : form}
        return render(request, 'index_login.html', context)


# delete_user
def delete_user(request, user_id):
    User.objects.filter(id=user_id).delete()
    return redirect('list_users')
