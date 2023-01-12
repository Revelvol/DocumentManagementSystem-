from django.shortcuts import render
from .forms import RegistrationForm,CustomUserForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout , get_user_model
from django.contrib.auth.models import  Group
from django.contrib import messages
from .models import User,Position , Departement
from django.contrib.auth.decorators import login_required
from .decorators import unauthenthicatedUser, allowedUsers
from django.http import JsonResponse
from django.contrib.auth.password_validation import ( MinimumLengthValidator,
                                                      CommonPasswordValidator,
                                                      NumericPasswordValidator,)
from django.core.exceptions import ValidationError
import json
# Create your views here.

def home(request):
    context ={}
    return render(request, 'base/home.html', context)

@allowedUsers('admins')
def userRegister(request):
    page = 'register'
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False) # make sure name is in lowercase
            user.name = user.name.lower()
            user.username = user.name
            user.save()
            group = Group.objects.get(name="staff")
            user.groups.add(group)
            return redirect ('editUserMenu')
        else:
            return messages.error(request, 'error has occured')
    context = {'form': form }
    return render (request, 'base/register.html',context)

def userLogout(request):
    logout(request)
    return redirect('home')
@unauthenthicatedUser
def userLogin(request):
    page = 'login '
    form = RegistrationForm()
    if request.method == "POST":
        name = request.POST.get('name').lower()
        password = request.POST.get('password')
        #masukin try block dlo untuk liat apakah user exist
        try:
            user = User.objects.get(name=name)
        except:
            messages.error(request,'User does not exist')
        user = authenticate(name = name, password = password)
        if user is not None :
            login(request, user )
            return redirect('home')
        else:
            messages.error(request,' password is wrong ')
    context= {'form' : form}
    return render ( request, 'base/login.html', context)

@login_required(login_url= 'userLogin')
def editUserMenu(request): #perlu decorator lagi buat pastiin dia admin doang
    user = get_user_model()
    users = user.objects.all().order_by('name')
    context = {'users': users}
    return render(request, 'base/editProfileMenu.html', context)
@login_required(login_url= 'userLogin')
@allowedUsers('admins')
def editUser(request, pk ): #perlu decorator lagi buat pastiin dia admin doang
    user = User.objects.get( id = pk)
    form = CustomUserForm(instance=user)
    # ga ush masukin if user.id = request.id
    if request.method == "POST":
        #update the form with the new data
        form = CustomUserForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
            return redirect('editUserMenu')
    context = {'user': user, 'form': form}
    return render(request, 'base/editProfile.html', context)


@login_required(login_url= 'userLogin')
def viewUser(request, pk ):
    user = User.objects.get( id = pk)
    users = User.objects.all().exclude(id=pk)
    context = {'user':user , 'users':users}
    return render (request, 'base/viewProfile.html', context)

def password_validation(request):
    if request.method == "POST":
        password = json.load(request)['password']
        response = {}
        try:
            MinimumLengthValidator().validate(password)
            response['length'] = True
            try:
                CommonPasswordValidator().validate(password)
                response['common'] = True
            except:
                response['common'] = False

            try:
                NumericPasswordValidator().validate(password)
                response['numeric'] = True
            except:
                response['numeric'] = False
        except ValidationError as e:
            response['length'] = False

        return JsonResponse(response)
@login_required(login_url= 'userLogin')
@allowedUsers('admins')
def deleteUser(request,pk):
    if request.method == "POST":
        user = User.objects.get(id=pk)
        user.delete()
        return redirect('editUserMenu')

@login_required(login_url= 'userLogin')
@allowedUsers('admins','staff')
def editPosition(request):
    positions = Position.objects.all()
    departements = Departement.objects.all()
    context = {'positions': positions, 'departements': departements}
    return render(request,'base/editPosition.html', context )



