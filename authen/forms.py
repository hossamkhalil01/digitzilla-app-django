from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User

class RegistrationForm (UserCreationForm):
  
  
    email = forms.EmailField(required= True, label='Email', widget=forms.EmailInput)


    class Meta:
        model = User
        fields = ['email','name','password1', 'password2']


    def save(self,commit=True):
        
        # Save the user data
        user = User.objects.create_user(
            email = self.cleaned_data['email'] ,
            name = self.cleaned_data['name'],
            password = self.cleaned_data["password1"],

        )
        
        return user
