from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, ProfileImagenForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('home')



    else:
        form = UserRegisterForm()

    return render(
        request,
        'users/registration.html',
        {
            'title': 'Страница регистрации',
            'form': form
        }
    )


@login_required
def profile(request):
    if request.method == "POST":
        profileForm = ProfileImagenForm(
            request.POST,
            request.FILES,
            instance=request.user.profile)
        updateUserForm = UserUpdateForm(
            request.POST,
            instance=request.user)
        if profileForm.is_valid() and updateUserForm.is_valid():
            updateUserForm.save()
            profileForm.save()
            messages.success(request, f'Выша акаунт был успешно обновлен!')
            return redirect('profile')

    else:
        profileForm = ProfileImagenForm(instance=request.user.profile)
        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm
    }

    return render(request, 'users/profile.html', data)
