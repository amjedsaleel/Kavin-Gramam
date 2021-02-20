# Django
from django import forms

# local Django
from . models import Member, HouseMember, Need


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


class RequirementForm(forms.ModelForm):
    class Meta:
        widgets = {
            'requirement': forms.CheckboxSelectMultiple()
        }
        model = Need
        fields = ['requirement']


class MemberFamilyForm(forms.ModelForm):
    class Meta:
        model = HouseMember
        fields = ['name', 'age', 'job', 'relationship']
