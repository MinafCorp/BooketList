from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user.models import User
import json

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    role = request.POST['role']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            if user.role != role:
                return JsonResponse({
                    "status": False,
                    "message": "Login gagal, role tidak sesuai."
                }, status=401)
            auth_login(request, user)
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!",
                "role" : user.role,
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun nonaktif."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal,periksa kembali username dan password anda."
        }, status=401)
        
        
@csrf_exempt
def logout(request):
    username = request.user.username
    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
     
     
@csrf_exempt
def register(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        
        username = data['username']
        email = data['email']
        password = data['password']
        first_name = data['first_name']
        last_name = data['last_name']
        password1 = data['password1']
        password2 = data['password2']
        role = data['role']
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({"status": False,"message": "Username sudah terdaftar."}, status=401)
            
        if password1 != password2: 
            return JsonResponse({"status": False,"message": "Password tidak Valid."}, status=401)
        
        create_user = User.objects.create_user(username=username, 
                                               email=email, 
                                               password=password, 
                                               first_name=first_name, 
                                               last_name=last_name,
                                               role=role)
        
        create_user.save()
        if role == 'AUTHOR':
            Author = Author.objects.create(user=create_user)
            Author.save()
        elif role == 'READER':
            Reader = Reader.objects.create(user=create_user)
            Reader.save()
            
        return JsonResponse({"status": True,"message": "Register berhasil."}, status=200)
    else :
        return JsonResponse({"status": False,"message": "Register gagal."}, status=401)