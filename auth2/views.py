from django.shortcuts import HttpResponseRedirect, redirect, render
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Bonjour {username}, Votre compte est bien créé, vous pouvez vous connecter !!'
            )
            return redirect('/')
        else:
            return render(request, 'registration/register.html', {'form': form})

    else:
        form = UserRegisterForm()
        return render(request, 'registration/register.html', {'form': form})
 

@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('/')