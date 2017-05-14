# -*- coding: utf-8 -*-
####################
# Python imports

####################
# Django imports
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
####################
# forms
from .forms import AddUserPostForm, AddCandidatePostForm, SchoolsForm, ProfilesForm
from .forms import LoginForm, LanguagesForm, SubjectsForm, EditUserForm
####################
# models
from django.contrib.auth.models import User
from .models import Candidate, Schools, Profiles, Languages, Subjects

##############################################################################
# views
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
        context = {'form': form}
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
    context = {'action': 'logout'}
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
    context = {
        'all_users': all_users,
        'users_count': users_count,
        'message_list_header': u'Lista użytkowników',
        'add_new_href': 'add_user',
        'add_new_text': u'Dodaj nowego użytkownika',
        'submit_button_text': 'Dodaj',
        'is_admin': is_admin
    }
    return render(request, "list_users.html", context)

####################
# add_user


@login_required(login_url='/')
def add_user(request):
    if request.method == 'POST':
        form = AddUserPostForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(request.POST['password'])
            if 'is_staff' in request.POST:
                new_user.is_staff = True
            new_user.save()
            return redirect('list_users')
    else:
        form = AddUserPostForm()
        context = {'form': form,
                   'message_add_new': u'Dodaj nowego użytkownika',
                   'submit_button_text': 'Dodaj',
                   'form_action_view': 'add_user'
                   }
        return render(request, "add.html", context)

####################
# delete_user


@login_required(login_url='/')
def delete_user(request, user_id):
    User.objects.filter(id=user_id).delete()
    return redirect('list_users')

####################
# edit user
@login_required(login_url='/')
def edit_user(request, user_id):
    user_instance = User.objects.get(pk=user_id)
    if request.method == 'POST':
        form_data = EditUserForm(request.POST, instance=user_instance)
        form_data.save()
        return redirect('list_users')
    else:
        form = EditUserForm(instance=user_instance)
        context = {
            'form': form,
            'message_add_new': u'Edytuj użytkownika {}'.format(user_instance.username),
            'submit_button_text': u'Edytuj',
            'form_action_view': 'edit_user/{}'.format(user_instance.id),
        }
        return render(request, "add.html", context)

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
        'all_candidates': all_candidates,
        'candidates_count': candidates_count,
        'message_list_header': u'Lista kandydatów',
        'add_new_href': 'add_candidate',
        'add_new_text': u'Dodaj nowego kandydata',
        'is_admin': is_admin
    }
    return render(request, "list_candidates.html", context)

####################
# add_candidate
@login_required(login_url='/')
def add_candidate(request):
    if request.method == 'POST':
        form = AddCandidatePostForm(request.POST, request.FILES)
        print(request.FILES['photo'])
        if form.is_valid():
            new_candidate = form.save(commit=False)
            # primary_school
            new_candidate.primary_school = Profiles.objects.get(
                pk=request.POST['primary_school']
            )
            # secondary_school
            new_candidate.secondary_school = Profiles.objects.get(
                pk=request.POST['secondary_school']
            )
            # third_school
            new_candidate.third_school = Profiles.objects.get(
                pk=request.POST['third_school']
            )
            #gim_language1
            new_candidate.gim_language1 = Languages.objects.get(
                pk=request.POST['gim_language1']
            )
            # gim_language2
            new_candidate.gim_language2 = Languages.objects.get(
                pk=request.POST['gim_language2']
            )
            # primary_language
            new_candidate.primary_language = Languages.objects.get(
                pk=request.POST['primary_language'])
            # secondary_language
            new_candidate.secondary_language = Languages.objects.get(
                pk=request.POST['secondary_language'])
            # subject_one
            new_candidate.subject_one = Subjects.objects.get(
                pk=request.POST['subject_one'])
            # subject_two
            new_candidate.subject_two = Subjects.objects.get(
                pk=request.POST['subject_two'])
            # subject_three
            new_candidate.subject_three = Subjects.objects.get(
                pk=request.POST['subject_three'])
            # photo
            new_candidate.photo = request.FILES['photo']
            # active_school
            new_candidate.active_school = new_candidate.primary_school

            new_candidate.save()
            return redirect('list_candidates')
        else:
            return render(request, "add.html", {'form': form, 'message_add_new': u'Dodaj nowego Kandydata', 'form_action_view': 'add_candidate'})
    else:
        form = AddCandidatePostForm()
        context = {'form': form,
                   'message_add_new': u'Dodaj nowego Kandydata',
                   'submit_button_text': 'Dodaj',
                   'form_action_view': 'add_candidate'
                   }
        return render(request, "add.html", context)

####################
# delete_candidate
def delete_candidate(request, candidate_id):
    Candidate.objects.filter(id=candidate_id).delete()
    return redirect('list_candidates')

####################
# edit candidate
@login_required(login_url='/')
def edit_candidate(request, candidate_id):
    object_instance = Candidate.objects.get(pk=candidate_id)
    if request.method == 'POST':
        form_data = AddCandidatePostForm(request.POST, request.FILES, instance=object_instance)
        form_data.save()
        return redirect('list_candidates')
    else:
        form = AddCandidatePostForm(instance=object_instance)
        context = {
            'form': form,
            'message_add_new': u'Edytuj kandydata {}'.format(object_instance.name),
            'submit_button_text': u'Edytuj',
            'form_action_view': 'edit_candidate/{}'.format(object_instance.id),
        }
        return render(request, "add.html", context)

####################
# edit candidate's active school
@login_required(login_url='/')
def edit_active_school(request, candidate_id, active_school):
    object_instance = Candidate.objects.get(pk=candidate_id)
    object_instance.active_school = Profiles.objects.get(pk=active_school)
    object_instance.save()
    return redirect('list_candidates')


##############################################################################
# SCHOOLS
##############################################################################
####################
# list_schools
@login_required(login_url='/')
def list_schools(request):
    all_schools = Schools.objects.order_by('id')
    schools_count = all_schools.count()
    is_admin = request.user.is_staff
    context = {
        'all_schools': all_schools,
        'schools_count': schools_count,
        'message_list_header': u'Lista szkół',
        'add_new_href': 'add_school',
        'add_new_text': u'Dodaj nową szkołę',
        'is_admin': is_admin
    }
    return render(request, "list_schools.html", context)

####################
# add_school
@login_required(login_url='/')
def add_school(request):
    if request.method == 'POST':
        form = SchoolsForm(request.POST)
        if form.is_valid():
            new_school = form.save(commit=False)
            new_school.name = request.POST['name']
            if request.POST['is_available'] == "on":
                new_school.is_available = True
            else:
                new_school.is_available = False
            new_school.save()
            return redirect('list_schools')
    else:
        form = SchoolsForm()
        context = {'form': form,
                   'message_add_new': u'Dodaj nową Szkołę',
                   'submit_button_text': 'Dodaj',
                   'form_action_view': 'add_school'
                   }
        return render(request, "add.html", context)

####################
# delete_school
@login_required(login_url='/')
def delete_school(request, school_id):
    Schools.objects.filter(id=school_id).delete()
    return redirect('list_schools')

####################
# edit school
@login_required(login_url='/')
def edit_school(request, school_id):
    object_instance = Schools.objects.get(pk=school_id)
    if request.method == 'POST':
        form_data = SchoolsForm(request.POST, instance=object_instance)
        form_data.save()
        return redirect('list_schools')
    else:
        form = SchoolsForm(instance=object_instance)
        context = {
            'form': form,
            'message_add_new': u'Edytuj szkołę',
            'submit_button_text': u'Edytuj',
            'form_action_view': 'edit_school/{}'.format(object_instance.id),
        }
        return render(request, "add.html", context)

##############################################################################
# LANGUAGES
##############################################################################
####################
# list_languages
@login_required(login_url='/')
def list_languages(request):
    all_languages = Languages.objects.order_by('id')
    languages_count = all_languages.count()
    is_admin = request.user.is_staff
    context = {
        'all_languages': all_languages,
        'is_admin': is_admin,
        'message_list_header': u'Lista języków obcych',
        'add_new_href': 'add_language',
        'add_new_text': u'Dodaj nowy język',
        'languages_count': languages_count
    }
    return render(request, "list_languages.html", context)

####################
# delete_language
@login_required(login_url='/')
def delete_language(request, language_id):
    Languages.objects.filter(id=language_id).delete()
    return redirect('list_languages')

####################
# add_language
@login_required(login_url='/')
def add_language(request):
    if request.method == 'POST':
        form = LanguagesForm(request.POST)
        if form.is_valid():
            new_lang = form.save(commit=False)
            if request.POST['is_available'] == "on":
                new_lang.is_available = True
            else:
                new_lang.is_available = False
            new_lang.save()
            return redirect('list_languages')
    else:
        form = LanguagesForm()
        context = {'form': form,
                   'message_add_new': u'Dodaj nowy Język',
                   'submit_button_text': 'Dodaj',
                   'form_action_view': 'add_language'
                   }
        return render(request, "add.html", context)

####################
# edit language
@login_required(login_url='/')
def edit_language(request, language_id):
    object_instance = Languages.objects.get(pk=language_id)
    if request.method == 'POST':
        form_data = LanguagesForm(request.POST, instance=object_instance)
        form_data.save()
        return redirect('list_languages')
    else:
        form = LanguagesForm(instance=object_instance)
        context = {
            'form': form,
            'message_add_new': u'Edytuj język',
            'submit_button_text': u'Edytuj',
            'form_action_view': 'edit_language/{}'.format(object_instance.id),
        }
        return render(request, "add.html", context)


##############################################################################
# PROFILES
##############################################################################
####################
# list_profiles
@login_required(login_url='/')
def list_profiles(request):
    all_profiles = Profiles.objects.order_by('id')
    profiles_count = all_profiles.count()
    is_admin = request.user.is_staff
    context = {
        'all_profiles': all_profiles,
        'is_admin': is_admin,
        'message_list_header': u'Lista profili kształcenia',
        'add_new_href': 'add_profile',
        'add_new_text': u'Dodaj nowy profil',
        'profiles_count': profiles_count
    }
    return render(request, "list_profiles.html", context)

####################
# delete_profile
@login_required(login_url='/')
def delete_profile(request, profile_id):
    Profiles.objects.filter(id=profile_id).delete()
    return redirect('list_profiles')

####################
# add_profile
@login_required(login_url='/')
def add_profile(request):
    if request.method == 'POST':
        form = ProfilesForm(request.POST)
        if form.is_valid():
            new_object = form.save(commit=False)
            new_object.school_id = Schools.objects.get(
                pk=request.POST['school_id'])
            new_object.shortcut = "{}-{}".format(request.POST['shortcut'], new_object.school_id.shortcut)
            if request.POST['is_available'] == "on":
                new_object.is_available = True
            else:
                new_object.is_available = False
            new_object.save()
            return redirect('list_profiles')
    else:
        form = ProfilesForm
        context = {'form': form,
                   'message_add_new': u'Dodaj nowy Profil',
                   'submit_button_text': 'Dodaj',
                   'form_action_view': 'add_profile'
                   }
        return render(request, "add.html", context)

####################
# edit profile
@login_required(login_url='/')
def edit_profile(request, profile_id):
    object_instance = Profiles.objects.get(pk=profile_id)
    if request.method == 'POST':
        form_data = ProfilesForm(request.POST, instance=object_instance)
        form_data.save()
        return redirect('list_profiles')
    else:
        form = ProfilesForm(instance=object_instance)
        context = {
            'form': form,
            'message_add_new': u'Edytuj profil',
            'submit_button_text': u'Edytuj',
            'form_action_view': 'edit_profile/{}'.format(object_instance.id),
        }
        return render(request, "add.html", context)


##############################################################################
# SUBJECTS
##############################################################################
####################
# list_subjects
@login_required(login_url='/')
def list_subjects(request):
    all_subjects = Subjects.objects.order_by('id')
    subjects_count = all_subjects.count()
    is_admin = request.user.is_staff
    context = {
        'all_subjects': all_subjects,
        'is_admin': is_admin,
        'message_list_header': u'Lista punktowanych przedmiotów',
        'add_new_href': 'add_subject',
        'add_new_text': u'Dodaj nowy przedmiot',
        'subjects_count': subjects_count
    }
    return render(request, "list_subjects.html", context)

####################
# delete_subject
@login_required(login_url='/')
def delete_subject(request, subject_id):
    Subjects.objects.filter(id=subject_id).delete()
    return redirect('list_subjects')

####################
# add_subject
@login_required(login_url='/')
def add_subject(request):
    if request.method == 'POST':
        form = SubjectsForm(request.POST)
        if form.is_valid():
            new_object = form.save(commit=False)
            if request.POST['is_available'] == "on":
                new_object.is_available = True
            else:
                new_object.is_available = False
            new_object.save()
            return redirect('list_subjects')
    else:
        form = SubjectsForm()
        context = {'form': form,
                   'message_add_new': u'Dodaj nowy Przedimot',
                   'submit_button_text': 'Dodaj',
                   'form_action_view': 'add_subject'
                   }
        return render(request, "add.html", context)

####################
# edit subject
@login_required(login_url='/')
def edit_subject(request, subject_id):
    object_instance = Subjects.objects.get(pk=subject_id)
    if request.method == 'POST':
        form_data = SubjectsForm(request.POST, instance=object_instance)
        form_data.save()
        return redirect('list_subjects')
    else:
        form = SubjectsForm(instance=object_instance)
        context = {
            'form': form,
            'message_add_new': u'Edytuj przedmiot',
            'submit_button_text': u'Edytuj',
            'form_action_view': 'edit_subject/{}'.format(object_instance.id),
        }
        return render(request, "add.html", context)
