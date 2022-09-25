from django import forms
from django.core import validators
from first_app.models import User, UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("need to start with z")
    
class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your Email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        
        if email != vmail:
            raise forms.ValidationError('Please ensure email match')

    
    #Saving Data to models
class NewUserForm(forms.ModelForm):
        class Meta:
            model = User
            fields = '__all__' 
