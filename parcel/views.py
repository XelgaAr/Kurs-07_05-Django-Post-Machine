# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

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


