from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':20,'b':30,'c':500}
    return render(request,'conditions.html',context=d)