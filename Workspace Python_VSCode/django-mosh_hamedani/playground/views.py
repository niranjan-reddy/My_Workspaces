from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    x = 1
    y = 2
    return x

# Create your views here.
def say_hello(request):
    x = calculate()
    y = 2

    # The following returns the Http Response as response body
    #return HttpResponse('Hello World')

    # The following returns the Django HTML Template (View/HTML Page) as response
    return render(request, 'hello.html', {'name': "Niranjan Reddy"})