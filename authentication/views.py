from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from user.forms import ReaderSignUpForm, AuthorSignUpForm

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
@require_http_methods(["POST"])
def register(request):
    data = request.POST
    role = data.get('role', '').upper()
    form = None 
    
    if role == 'READER':
        form = ReaderSignUpForm(data)
    elif role == 'AUTHOR':
        form = AuthorSignUpForm(data)
    else:
        return JsonResponse({
            "status": False,
            "message": "Role tidak valid/tidak ada."
        }, status=400)
        
    if form and form.is_valid():
        user = form.save()
        return JsonResponse({
            "username": user.username,
            "status": True,
            "message": "Register berhasil!"
        }, status=200)
    else:
        return JsonResponse({
            "status": False,
            "message": "Register gagal."
        }, status=400)