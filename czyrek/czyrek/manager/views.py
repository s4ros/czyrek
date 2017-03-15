####################
## Python imports

####################
## Django imports
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
####################
## forms
from .forms import AddUserPostForm, AddCandidatePostForm
from .forms import LoginForm
####################
## models
from django.contrib.auth.models import User
from .models import Candidate, Schools, Profiles, Languages, Subjects

##############################################################################
## views
##############################################################################

##############################################################################
# GENERAL VIEWS
##############################################################################

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
# index after login
@login_required(login_url='/')
def index_after_login(request):
    return render(request, "index.html")

####################
# user logout
@login_required(login_url='/')
def logout_user(request):
    logout(request)
    context = { 'action': 'logout' }
    return redirect('index_login')

##############################################################################
# USERS
##############################################################################

####################
# list_users
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
        form = AddUserPostForm(request.POST)
        if form.is_valid():
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
# delete_user
@login_required(login_url='/')
def delete_user(request, user_id):
    User.objects.filter(id=user_id).delete()
    return redirect('list_users')

##############################################################################
# CANDIDATES
##############################################################################

####################
# list_candidates
@login_required(login_url='/')
def list_candidates(request):
    all_candidates = Candidate.objects.order_by('id')
    candidates_count = all_candidates.count()
    is_admin = request.user.is_staff
    context = {
                'all_candidates' : all_candidates,
               'candidates_count' : candidates_count,
               'is_admin' : is_admin
               }
    return render(request, "list_candidates.html", context)

####################
# add_candidate
@login_required(login_url='/')
def add_candidate(request):
    if request.method == 'POST':
        form = AddCandidatePostForm(request.POST)
        if form.is_valid():
            new_candidate = form.save(commit=False)
            new_candidate.name = request.POST['name']
            new_candidate.surname = request.POST['surname']
            new_candidate.city = request.POST['city']
            new_candidate.address = request.POST['address']
            new_candidate.postalcode = request.POST['postalcode']
            new_candidate.voivodeship = request.POST['voivodeship']
            new_candidate.community = request.POST['community']
            new_candidate.phone = request.POST['phone']
            new_candidate.pesel = request.POST['pesel']
            new_candidate.birthdate = request.POST['birthdate']
            new_candidate.last_school = request.POST['last_school']
            new_candidate.primary_language = request.POST['primary_language']
            new_candidate.secondary_language = request.POST['secondary_language']
            new_candidate.subject_one = request.POST['subject_one']
            new_candidate.subject_two = request.POST['subject_two']
            new_candidate.subject_three = request.POST['subject_three']
            new_candidate.photo = request.POST['photo']
            new_candidate.save()
            return redirect('list_candidates')
        else:
            return render(request, "add_candidate.html", {'form':form})
    else:
        form = AddCandidatePostForm()
        context = {'form' : form}
        return render(request, "add_candidate.html", context)

####################
# delete_candidate
def delete_candidate(request, candidate_id):
    Candidate.objects.filter(id=candidate_id).delete()
    return redirect('list_candidates')

##############################################################################
# SCHOOLS
##############################################################################

####################
# list_schools
@login_required(login_url='/')
def list_schools(request):
    all_schools = Schools.objects.order_by('id')
    is_admin = request.user.is_staff
    context = {
        'all_schools' : all_schools,
        'is_admin' : is_admin
    }
    return render(request, "list_schools.html", context)

##############################################################################
# LANGUAGES
##############################################################################

####################
# list_languages
@login_required(login_url='/')
def list_languages(request):
    context = {}
    return render(request, "list_languages.html", context)

##############################################################################
# PROFILES
##############################################################################

####################
# list_profiles
@login_required(login_url='/')
def list_profiles(request):
    context = {}
    return render(request, "list_profiles.html", context)

##############################################################################
# SUBJECTS
##############################################################################

####################
# list_subjects
@login_required(login_url='/')
def list_subjects(request):
    context = {}
    return render(request, "list_subjects.html", context)
