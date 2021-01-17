from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import advertisment,contactmodel,extenduser
class user_signupk(UserCreationForm):
    username= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'RISHAV'}))
    #phone= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': '7667805324'}))
    #email = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'rishavranjan700@gmail.com'}))
    password1=forms.CharField(label='psfirsebtao',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'ENTER PASSWORD'}))
    password2=forms.CharField(label='passfirsebtao',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'RENTER PASSWORD'}))
    class Meta:
        model = User
        fields = ['username','password1','password2']

class userprofile(forms.ModelForm):
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': '7667805324'}))
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'MIRZAPUR'}))
    state = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'JHARKHAND'}))
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'rishavranjan700@gmail.com'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'RISHAV'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'RANJAN'}))
    class Meta:
        model=extenduser
        fields=['first_name','last_name','phone','email','city','state']
   


class user_logink(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'RISHAV77'}))
    password=forms.CharField(label="btao Password",widget=forms.PasswordInput(attrs={'class': "form-control" ,'placeholder': 'password'}))
class shows(forms.ModelForm):
    title= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control ti",'placeholder': 'title'}))
    description = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control de",'placeholder':'description'}))
    state = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control de",'placeholder': 'JHARKHAND'}))
    district = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control de",'placeholder': 'MIRZAPUR'}))
    bedroom = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': "form-control de",'placeholder': '4'}),error_messages={'invalid':'Enter a valid bedrrom'})
    
    bathroom= forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': "form-control de",'placeholder': '1'}),error_messages={'invalid':'Enter a valid bathroom'})
    cost= forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': "form-control de",'placeholder': '2000000'}),error_messages={'invalid':'Enter a valid cost'})
    #user = forms.CharField(widget=forms.HiddenInput(), initial="rishav")
    #user=forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'putuser','placeholder':''})
    #user=forms.TextInput(attrs={'class': "form-control de" ,'id':'putuser','disabled': 'disabled','placeholder':''})
    #user= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control ti",'value': '', 'id': 'putuser','placeholder':''}))
    class Meta:
        model=advertisment
        fields='__all__'
        exclude=('date','user','view_count')
        
class contactshows(forms.ModelForm):
    phone= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': '7667805624'}))
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'rishavranjan700@gmail.com'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'SUBJECT'}))
    message = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control",'placeholder': 'message'}))
    
    class Meta:
        model=contactmodel
        fields='__all__'
