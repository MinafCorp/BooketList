from django.shortcuts import render
from user.forms import UserForm
from django.shortcuts import redirect

# Create your views here.
def show_landing(request):
    return render(request, 'landing.html')

def register(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')
    context = {'form':form}
    return render(request, 'signup.html', context)