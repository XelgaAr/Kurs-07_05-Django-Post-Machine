from django.shortcuts import render
# from django.shortcuts import render
from django.http import HttpResponse
from post_machine import models

def post_machine_view(request):
    # return render(request, 'parcels.html')
    return HttpResponse("hello,world.Post Machine view")


def one_post_machine_view(request, machine_id):
    # return render(request, 'one_parcel.html')
    return HttpResponse("hello,world.One Post Machine view")


def locker_view(request, machine_id):
    one_post_machine = models.PostMachine.objects.get(id=machine_id)
    post_machine_locker = models.Locker.objects.filter(post_machine=one_post_machine)
    one_locker = models.Locker.objects.get(pk=5)
    return HttpResponse(f"ok, {[itm.id for itm in post_machine_locker]}")