from tokenize import PseudoExtras
from django.shortcuts import redirect, render
<<<<<<< HEAD:ludoscienceapp/views/admin.py
from ludoscienceapp.models.user import User
from ludoscienceapp.models.role import Role
from ludoscienceapp.models.token import Token
from ludoscienceapp.utils.System import System
=======
from creativescienceapp.models.user import User
from creativescienceapp.models.role import Role
from creativescienceapp.models.token import Token
from creativescienceapp.utils.System import System
>>>>>>> fc50664f765aba41ae26cac3f94c5b094dfcf932:creativescienceapp/views/admin.py
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from werkzeug.security import generate_password_hash,check_password_hash


def register_admin(request):
  
    if User.objects.filter(email__exact=request.POST['email']).exists() or  User.objects.filter(username__exact=request.POST['username']).exists():
        messages.error(request,'Nombre de usuario/email ya registrado')
        return redirect('create_admin')
    if not request.POST['email'] or not request.POST['username'] or not request.POST['password'] or not request.POST['repeat_password'] or not request.POST['name'] or (request.POST['password'] != request.POST['repeat_password']):
        if (request.POST['password'] != request.POST['repeat_password']):
            messages.error(request,'Las contraseñas no coinciden')
        else:
            messages.error(request,'Todos los campos deben estar completos')
        return redirect('create_admin')
        
    user=User(email=request.POST['email'],username=request.POST['username'],complete_name=request.POST['name'],role_id=Role.objects.get(name='ADMIN'),password=generate_password_hash(request.POST['password'], 'sha256', 10))
    user.save()
    messages.success(request,'¡Administrador dado de alta con éxito')
    return redirect('create_admin')
    #System.set_session(request,user)  
    #return user_verificate(request,True,user)

def create_admin(request):
     if System.is_logged(request):
          if System.is_root(request):
            return render (request,'ludoscienceapp/create_admin.html',{'nav':'block','create_admin':System.get_navbar_color})      
          redirect('home')
     return redirect('index')  

