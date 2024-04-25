from django import forms
from django.contrib.auth.forms import *
from .models import *
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _

class OrderInfoForm(forms.ModelForm):
    class Meta:
        model = OrderInfo
        fields = ['id', 'deliver_name', 'client', 'price', 'sity', 'street', 'home', 'entrance', 'floor', 'flat', 'comment', 'status']

class UserCreatForm(UserCreationForm):
   email = forms.EmailField(required=True, label=_("Email"))
    
   class Meta(UserCreationForm.Meta):
      fields = UserCreationForm.Meta.fields + ('email',)
      
   password1 = forms.CharField(
      label=_("Password"),
      strip=False,
      widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
      help_text=password_validation.password_validators_help_text_html(),
   )
   password2 = forms.CharField(
      label=_("Password confirmation"),
      strip=False,
      widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
      help_text=_("Введите пароль ещё раз."),
   )
   
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['username'].help_text = _("Только буквы, цифры и символы @/./+/-/_.")
      self.fields['password1'].help_text = _("Пароль должен включать в себя не менее 8 символов, состоящий хотя бы из букв и цифр")
      self.fields['password2'].help_text = _("Введите пароль ещё раз.")
      self.fields['email'].help_text = _("")