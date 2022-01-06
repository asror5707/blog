from django.shortcuts import render

from .models import Maqola,Rasm

def home(request):
    return render(request,'home.html')
def blog(request):
    maqola = Maqola.objects.all().order_by("-time")
    return render(request,'blog.html',{'maqola':maqola})
def maqola1(request,son):
    maqola = Maqola.objects.get(id = son)
    rasm = Rasm.objects.filter(maqola=maqola)
    return render(request, 'maqola.html', {'m': maqola, 'r':rasm})
def maqola(request):
    return render(request,'maqola.html')
def about(request):
    return render(request,'about.html')

# Create your views here.
