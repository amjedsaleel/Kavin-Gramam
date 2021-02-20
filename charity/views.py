# Django
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.urls import reverse

# local Django
from .forms import MemberForm, RequirementForm
from .models import Member, HouseMember, Category, Need


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
    needs = Need.objects.filter(requirement=category)
    print(needs)

    context = {
        'requirements': needs,
        'category': category,
        'total_members': needs.count()
    }

    return render(request, 'charity/view-by-category.html', context)


def view_all_members(request):
    members = Member.objects.all()

    context = {
        'members': members,
    }
    return render(request, 'charity/view-all-members.html', context)


def view_member(request, id):
    member = Member.objects.get(id=id)
    house_members = member.housemember_set.all()

    member_form = MemberForm(instance=member)
    requirements_form = RequirementForm(instance=member.need)

    context = {
        'member': member,
        'house_members': house_members,
        'member_form': member_form,
        'requirements_form': requirements_form,
    }

    return render(request, 'charity/member-detail.html', context)


def update_member_personal_info(request, id):

    if request.method == 'POST':
        member = Member.objects.get(id=id)
        form = MemberForm(request.POST, instance=member)
        print(form.errors)

        if form.is_valid():
            form.save()
            return redirect(reverse('charity:view-member', args=id))

        print('form not valid')
        return redirect(reverse('charity:view-member', args=id))


def update_member_requirements(request, id):

    if request.method == 'POST':
        member = Member.objects.get(id=id).need
        form = RequirementForm(request.POST, instance=member)

        if form.is_valid():
            form.save()
            return redirect(reverse('charity:view-member', args=id))

        return redirect(reverse('charity:view-member', args=id))
