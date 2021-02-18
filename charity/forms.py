# Django
from django import forms

# local Django
from . models import Member, HouseMember


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
