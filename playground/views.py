from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def say_hello(request):
    # pull data from db
    # transform data
    # send emails ans so on
    # lets do a simple response
    # return HttpResponse("Hello World") 
    # return render(request, 'hello.html')
    return render(request, 'hello.html', {'name': 'My name is Abdul'})