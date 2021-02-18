# Django
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

# local Django
from .forms import MemberForm
from .models import Member, HouseMember


# Create your views here.


def index(request):
    return render(request, 'charity/index.html')


def add_member(request):
    member_form = MemberForm()
    house_member_formset = inlineformset_factory(Member, HouseMember, fields=('name', 'age', 'job', 'relationship'),
                                                 extra=6, can_delete=False)
    if request.method == 'POST':
        form = MemberForm(request.POST)

        if form.is_valid():
            instance = form.save()
            formset = house_member_formset(request.POST, instance=instance)

            if formset.is_valid():
                formset.save()

            return redirect('charity:add-member')

    formset = house_member_formset()

    context = {
        'member_form': member_form,
        'formset': formset
    }

    return render(request, 'charity/add-member.html', context)
