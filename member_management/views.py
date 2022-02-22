from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models


def index(request):
    members = models.Member.objects.all()
    context = {'members': members}
    return render(request, 'index.html', context)


def add(request):
    # TODO check for admin status
    if request.method == 'POST':
        form = models.MemberForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            surname = form.cleaned_data.get('surname')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            role = form.cleaned_data.get('role')
            new_member = models.Member()
            # TODO cleanup
            new_member.first_name = first_name
            new_member.surname = surname
            new_member.email = email
            new_member.phone_number = phone_number
            new_member.role = role
            new_member.full_clean()
            new_member.save()
            return redirect('/')
        else:
            context = {'form': form}
    else:
        form = models.MemberForm()
        context = {'form': form}
    return render(request, 'add.html', context)


def edit(request, member_id):
    # TODO check for admin status
    try:
        member = models.Member.objects.get(id=member_id)
    except models.Member.DoesNotExist:
        return redirect('/not-found')
    if request.method == 'POST':
        form = models.MemberForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            surname = form.cleaned_data.get('surname')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            role = form.cleaned_data.get('role')
            # TODO cleanup
            member.first_name = first_name
            member.surname = surname
            member.email = email
            member.phone_number = phone_number
            member.role = role
            member.full_clean()
            member.save()
            return redirect('/')
        else:
            context = {'form': form}
    else:
        form = models.MemberForm(instance=member)
        context = {'form': form, 'member': member}
    return render(request, 'edit.html', context)


def unknown_path(request, path):
    return HttpResponse("404 error")
