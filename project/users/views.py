from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, FormView
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator as \
    token_generator
from users.forms import UserCreationForm, AuthenticationForm, CodeForm
from users.utils import send_email_for_verify



# todo: 
# -генератор пароля +
# -сохранение пароля в юсер(может и не надо/мб отдельную модель с паролями и исер вйди)+
# -сохраняем модель юсер+
# -отправка ппароля в письме+
# -реддирект на стр с формой ввода пароля+

# @login[-функчия проверки пароя (из письма вытащить юсер айди и код)
# -логиним юсера]



User = get_user_model()


class MyLoginView(LoginView):
    form_class = AuthenticationForm


class EmailVerify(View):
    form_class = CodeForm
    model = User
    template_name = 'registration/confirm_email.html'

    def get(self, request):
        context = {
            'form': CodeForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CodeForm(request.POST)

        if form.is_valid():
            # form.save()
            id = form.cleaned_data.get('id')
            user = User.objects.get(id=form.cleaned_data.get('id'))
            # user = authenticate(email=user_f.email, password=password)
            print( "verify", user)
            #user.save()
            if user is not None:
                code = form.cleaned_data.get('code')
                if code == user.code:
                    user.email_verify = True
                    user.save()

                    login(request, user)
                    return redirect('home')
            else:        
                return redirect('invalid_verify')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)    






    # функция либо get/dispatch
    # def get(self, request, *args, **kwargs):
    #     print('def_get')
    #     form = CodeForm(request.POST)
    #     print('form', form)
    #     if form.is_valid():
    #         print('valid')
    #         form.save()
    #         user = self.get_user(request)
    #         print('dispatch user', user)
    #         if user is not None:
    #             code = form.cleaned_data.get('code')
    #             if code == user.code:
    #                 email_verify = True
    #                 user.save()
    #                 login(request, user)
    #                 return redirect('home')
    #         return redirect('invalid_verify')




    # def get_user(self, request):
    #     if request.method == "POST":
    #             form = CodeForm(request.POST)
    #             form.save()
    #             if form.is_valid():
    #                 try:
    #                     user = User.objects.get(id=form.cleaned_data.get('id'))
    #                 except ():
    #                     user = None
    #                 return user  

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs["user"] = self.user
    #     return kwargs      

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            print( "views", user)
            #user.save()
            send_email_for_verify(request, user)
            return redirect('confirm_email') # стр введите пароль
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
