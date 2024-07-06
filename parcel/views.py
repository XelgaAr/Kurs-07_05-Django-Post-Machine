# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def parcels_view(request):
    # return render(request, 'parcels.html')
    return HttpResponse("hello,world.Parcels view")


def one_parcel_view(request, parcel_id):
    # return render(request, 'one_parcel.html')
    return HttpResponse("hello,world.One_Parcel view")
