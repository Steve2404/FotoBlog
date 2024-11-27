from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.views.generic import View

from authentication import forms
from authentication.forms import LoginForm, UploadProfilePhotoForm


# Create your views here.

# def logout_user(request):
#    logout(request)
#    return redirect('login')


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', {'form': form})


'''
class LoginPageView(View, ):
    template_name = 'authentication/login.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name,
                      context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            message = "Identifiants Invalides ..."
            return render(request, self.template_name,
                          context={'form': form, 'message': message})


'''


def upload_profile_photo(request):
    form = UploadProfilePhotoForm(instance=request.user)
    if request.method == 'POST':
        form = UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/upload_profile_photo.html', {'form': form})
