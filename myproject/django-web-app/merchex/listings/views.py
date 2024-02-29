
from django.shortcuts import render
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html',{'bands':bands})
   