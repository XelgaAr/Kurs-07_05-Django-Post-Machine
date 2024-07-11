from django.shortcuts import render
# from django.shortcuts import render
from django.http import HttpResponse
from post_machine import models


def post_machine_view(request):
    # return render(request, 'parcels.html')
    # return HttpResponse("hello,world.Post Machine view")
    post_machines = models.PostMachine.objects.all()
    return render(request, 'post_machines.html', {'post_machines': post_machines})


# def one_post_machine_view(request, machine_id):
#     # return render(request, 'one_parcel.html')
#     # return HttpResponse("hello,world.One Post Machine view")
#     one_post_machine = models.PostMachine.objects.get(id=machine_id)
#     lockers = one_post_machine.locker_set.all()
#     return render(request, 'one_post_machine.html', {'machine_id': machine_id, 'one_post_machine':one_post_machine, 'lockers': lockers})


def locker_view(request, machine_id):
    one_post_machine = models.PostMachine.objects.get(id=machine_id)
    post_machine_locker = models.Locker.objects.filter(post_machine=one_post_machine)
    lockers = one_post_machine.locker_set.all()
    # return HttpResponse(f"ok, {[itm.id for itm in post_machine_locker]}")
    return render(request, 'locker.html', {'machine_id': machine_id, 'one_post_machine':one_post_machine, 'post_machine_locker': post_machine_locker, 'lockers': lockers})
