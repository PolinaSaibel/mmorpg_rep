from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms


#переопределяем юзера в форме регисрации
User = get_user_model()


class UserCreationForm(UserCreationForm):
    #добавим email в форму регистрацции
    email = forms.EmailField(
        label= "Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")