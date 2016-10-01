from django.http import HttpResponse
from django_micro import Micro


app = Micro()


@app.route(r'^hello$', name='hello')
def print_hello(request):
    return HttpResponse('hello')
