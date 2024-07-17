# from django.shortcuts import render
import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from parcel import models
from parcel.form import ParcelForm
from parcel.models import Parcel


# Create your views here.

def parcels_view(request):
    # return render(request, 'parcels.html')
    user = request.user
    parcels = models.Parcel.objects.filter(recipient=user)
    return render(request, 'parcels.html', context={'parcels': parcels})


def one_parcel_view(request, parcel_id):
    # return render(request, 'one_parcel.html')
    result = models.Parcel.objects.get(pk=parcel_id)

    return render(request,"one_parcel.html", context={'parcel': result})

def get_parcel(request):
    if request.method == 'POST':
        parcel = Parcel.objects.get(pk=request.POST['parcel_id'])
        parcel.status = True

        parcel.open_datetime = datetime.datetime.now()
        if parcel.order_datetime is None:
            parcel.order_datetime = datetime.datetime.now()
        if parcel.update_datetime is None:
            parcel.update_datetime = datetime.datetime.now()
        parcel.save()

        parcel.locker.status = True
        parcel.locker.save()
        return redirect('/parcel/')




def parcel_form_test_update(request, obj_id):
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():
            first_parcel = models.Parcel.objects.get(pk=obj_id)
            first_parcel.form_client(form.cleaned_data)
            first_parcel.save()
            return HttpResponse('Form submitted successfully!')
        else:
            return HttpResponse('Form error')
    first_parcel = models.Parcel.objects.get(pk=obj_id)
    form = ParcelForm(first_parcel.to_client())
    return render(request, 'parcel_form.html', context={'form': form, 'obj_id':obj_id})


