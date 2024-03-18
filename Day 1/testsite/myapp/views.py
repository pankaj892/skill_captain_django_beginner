from django.http import HttpResponse

# Create your views here.

# Create a view called hello_world
def hello_world(request):
    return HttpResponse('Hello, World!')