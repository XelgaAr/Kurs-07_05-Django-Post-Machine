from django.shortcuts import HttpResponse


# Create your views here.
def user_page(request):
    return HttpResponse("hello,world.User page")
