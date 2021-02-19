# Django
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

# local Django
from .forms import MemberForm, RequirementForm
from .models import Member, HouseMember, Category, Requirement


# Create your views here.


def index(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'charity/index.html', context)


def add_member(request):
    member_form = MemberForm()
    house_member_formset = inlineformset_factory(Member, HouseMember, fields=('name', 'age', 'job', 'relationship'),
                                                 extra=6, can_delete=False)
    formset = house_member_formset()
    requirements_form = RequirementForm()

    if request.method == 'POST':
        member_form = MemberForm(request.POST)
        requirements_form = RequirementForm(request.POST)

        if member_form.is_valid() and requirements_form.is_valid():
            member_instance = member_form.save()  # Saved the all personal details of member
            formset = house_member_formset(request.POST, instance=member_instance)  # Saved all details members in house

            if formset.is_valid():
                formset.save()

            requirements_instance = requirements_form.save(commit=False)
            requirements_instance.member = member_instance
            requirements_instance.save()
            requirements_form._save_m2m()

            return redirect('charity:add-member')

    context = {
        'member_form': member_form,
        'formset': formset,
        'requirements': requirements_form
    }

    return render(request, 'charity/add-member.html', context)


def view_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    requirements = Requirement.objects.filter(requirement=category)
    print(requirements)

    context = {
        'requirements': requirements,
        'category': category,
        'total_members': requirements.count()
    }

    return render(request, 'charity/view-by-category.html', context)


def view_all_members(request):
    members = Member.objects.all()
    requirements = Requirement.objects.all()

    # memb = Member.objects.filter(requirement__in=[2,1,3])

    for member in members:
        print(member.name)
        for i in member.requirement_set.all():
            print('re:', i.requirement)

    # print(requirements)

    context = {
        'members': members,
        'requirements': requirements,
    }
    return render(request, 'charity/view-all-members.html', context)
