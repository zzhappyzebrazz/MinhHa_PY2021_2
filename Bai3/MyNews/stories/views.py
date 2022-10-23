from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    message = '''
    Hello from me to the other side <br>
    This is: <b>Stories for Children</b> app!
    '''
    return HttpResponse(message)
