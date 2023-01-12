from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User
from django.utils.safestring import mark_safe

class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['name', 'email', 'manager', 'position', 'password1', 'password2']:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
            if field_name == 'email':
                self.fields[field_name].widget.attrs.update({'placeholder': 'name@example.com'})
            if field_name == 'password1' :
                self.fields[field_name].widget.attrs.update({'onfocus': 'showPasswordValidator()',
                                                             'onblur': 'hidePasswordValidator()',
                                                             'onkeyup': 'validatePassword1()',

                                                             })
                self.fields[field_name].help_text = mark_safe(
                    '<div id="password-confirmation-message" class="password-confirmation-message">'  
                        '<p id="character-password" class="invalid"> <b> At least 8 characters </b> </p>'
                        '<p id="common-password" class="invalid"> <b> Can’t be a commonly used password.</b> </p>'
                        '<p id="number-password" class="invalid"> <b> Cant be entirely numeric</b> </p>'
                    '</div>'
                )
            if field_name == 'password2' :
                self.fields[field_name].widget.attrs.update({'onfocus': 'showPasswordValidator(), showPasswordValidator2()',
                                                             'onblur': 'hidePasswordValidator(), hidePasswordValidator2()',
                                                             'onkeyup': 'validatePassword2()',

                                                             })
                self.fields[field_name].help_text = mark_safe(
                    '<div id="password-confirmation-message2" class="password-confirmation-message">'  
                        '<p id="same-password" class="invalid"> <b> Must be the Same Password </b> </p>'
                    '</div>'
                )
    class Meta:
        model = User
        fields = ['name', 'email', 'manager',  'position']

class CustomUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'manager', 'position']
