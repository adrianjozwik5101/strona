from django import forms
from userprofile.models import UserProfile

class UsersProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('country','age','sex')