from django import forms
from gamelands.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('nickname','pfp','description')