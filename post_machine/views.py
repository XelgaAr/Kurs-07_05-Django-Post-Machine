from django.shortcuts import render
# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def post_machine_view(request):
    # return render(request, 'parcels.html')
    return HttpResponse("hello,world.Post Machine view")


def one_post_machine_view(request, machine_id):
    # return render(request, 'one_parcel.html')
    return HttpResponse("hello,world.One Post Machine view")
