from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Appointments
from ..logreg_app.models import User
from django.contrib import messages
from datetime import datetime, date
from django.db.models import Q
now = datetime.now()


def index(request):
    if 'id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session["id"])
    context = {
        "today": Appointments.objects.filter(Q(start_date__lte=now, start_date__gte=now) & Q(creator__full_name=request.session["full_name"])),
        "future": Appointments.objects.filter(creator__full_name=request.session["full_name"]).exclude(start_date__lte=now)
    }
    return render(request, 'appts_app/index.html', context)


def edit(request, appointment_id):
    if 'id' not in request.session:
        return redirect(reverse('logreg_app:index'))
    context = {
        "appointment": Appointments.objects.get(id=appointment_id),
        "users": User.objects.all()
    }
    return render(request, 'appts_app/edit.html', context)


def create(request):
    if 'id' not in request.session:
        return redirect(reverse('logreg_app:index'))

    if request.POST["start_date"] and request.POST["start_time"] and request.POST["task"]:
        user = User.objects.get(id=request.session['id'])
        task = request.POST["task"]
        start_date = datetime.strptime(request.POST["start_date"], '%Y-%m-%d')
        start_time = datetime.strptime(request.POST["start_time"], '%H:%M')
        today = datetime(year=now.year, month=now.month, day=now.day)
        if start_date >= today:
            appointment = Appointments.objects.create(
                task=task, start_date=start_date, start_time=start_time, creator=user)
            return redirect(reverse('appts_app:index'))
        else:
            messages.add_message(request, messages.SUCCESS, 'Try again')
            return redirect(reverse('appts_app:index'))
    else:
        messages.add_message(request, messages.SUCCESS, 'Try again')
        return redirect(reverse('appts_app:indexindex'))


def update(request, appointment_id):
    if 'id' not in request.session:
        return redirect(reverse('logreg_app:index'))
    if request.POST["start_date"] and request.POST["start_time"] and request.POST["task"] and request.POST["status"]:
        a = Appointments.objects.get(id=appointment_id)
        a.task = request.POST["task"]
        a.status = request.POST["status"]
        a.start_date = datetime.strptime(
            request.POST["start_date"], '%Y-%m-%d')
        a.start_time = datetime.strptime(request.POST["start_time"], '%H:%M')
        today = datetime(year=now.year, month=now.month, day=now.day)
        if a.start_date >= today:
            a.save()
        else:
            print a.start_time
            messages.add_message(request, messages.SUCCESS, 'Try again')
            a = Appointments.objects.get(id=appointment_id)
            return redirect(reverse('appts_app:edit', kwargs={"appointment_id": a.id}))
    else:
        messages.add_message(request, messages.SUCCESS, 'Try again')
        a = Appointments.objects.get(id=appointment_id)
        return redirect(reverse('appts_app:edit', kwargs={"appointment_id": a.id}))
    return redirect(reverse('appts_app:index'))


def delete(request, appointment_id):
    if 'id' not in request.session:
        return redirect(reverse('logreg_app:index'))

    context = {
        "appointment": Appointments.objects.get(id=appointment_id),
        "users": User.objects.all()
    }
    return render(request, 'appts_app/delete.html', context)


def destroy(request, appointment_id):
    if 'id' not in request.session:
        return redirect(reverse('logreg_app:index'))
    appointment = Appointments.objects.get(id=appointment_id)
    appointment.delete()
    return redirect(reverse('appts_app:index'))
