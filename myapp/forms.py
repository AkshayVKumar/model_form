from django import forms
from myapp.models import *
from django.core import validators
def check_for_A(s):
    if s[0].lower()!='a':
        raise forms.ValidationError("Name must start with A")

class ContactForm(forms.Form):
    Name=forms.CharField(min_length=4,max_length=40,required=True,\
        label="Name",validators=[check_for_A])
    Email=forms.EmailField(min_length=5,max_length=100,required=True,label="Email")
    ReEnter_Email=forms.EmailField(min_length=5,max_length=100,required=True)
    Phno=forms.CharField(required=True,max_length=10,min_length=10,\
        validators=[validators.RegexValidator('[6-9]\d{9}')])
    Commment=forms.CharField(widget=forms.Textarea)
    Gender=forms.ChoiceField(choices=(('Male','Male'),\
        ('Female','Female')),widget=forms.RadioSelect)
    Password=forms.CharField(min_length=4,max_length=10,\
        widget=forms.PasswordInput)
    botcacher=forms.CharField(required=False,widget=forms.HiddenInput,\
        validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        e=self.cleaned_data.get('Email')
        a=self.cleaned_data.get('ReEnter_Email')
        if e!=a:
            raise forms.ValidationError("Emails Not Matched")


class Access_Record_Form(forms.ModelForm):
    class Meta:
        model=Webpage
        #fields='__all__'
        #fields=('topic','name','url')
        exclude=('url',)