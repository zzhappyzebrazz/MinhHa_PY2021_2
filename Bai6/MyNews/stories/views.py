from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'stories/index.html')

def blog(request):
    return render(request, 'stories/blog.html')

def Contact_us(request):
    return render(request, 'stories/Contact_us.html')

def single(request):
    return render(request, 'stories/single.html')
