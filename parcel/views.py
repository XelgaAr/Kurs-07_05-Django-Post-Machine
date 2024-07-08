# from django.shortcuts import render
from django.http import HttpResponse
from parcel import models


# Create your views here.

def parcels_view(request):
    # return render(request, 'parcels.html')
    return HttpResponse("hello,world.Parcels view")


def one_parcel_view(request, parcel_id):
    # return render(request, 'one_parcel.html')
    result = models.Parcel.objects.get(pk=parcel_id)
    return HttpResponse("hello,world.One_Parcel view")
