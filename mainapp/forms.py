from django import forms
from django.contrib.auth.models import User
from mainapp.models import teaminfo

class TeamUserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model=User
        labels={'username':'Team Name','password':'Password'}
        fields=('username','email','password')

class TeamInfoForm(forms.ModelForm):
    class Meta():
        model=teaminfo
        fields=('member1_name','member1_rollno','member1_phone','member1_branch','member2_name','member2_rollno','member2_phone','member2_branch','collegename')
        labels={
                'member1_name':'Member1 Name',
                'member1_rollno':"Member1 Roll No.",
                'member1_phone':"Member1 Phone No.",
                'member1_branch':"Member1 Branch",
                'member2_name':'Member2 Name',
                'member2_rollno':"Member2 Roll No.",
                'member2_phone':"Member2 Phone No.",
                'member2_branch':"Member2 Branch",
                'collegename':'College Name',
                }
