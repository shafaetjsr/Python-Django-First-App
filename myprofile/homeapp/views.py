from django.shortcuts import render,HttpResponse

# Create your views here.
"""
def index(request):
    return HttpResponse('Hello Shafaet from home app in index Method')

def about(request):
    return HttpResponse('Hello Shafaet From home app about method')

def contact(request):
    return HttpResponse('Hello Shafaet From Home App in Contact Method')
    
"""

def index(request):
    context={'title':'Home'}
    return render(request,'homeapp/index.html',context)

def about(request):
    context={'title':'About'}
    return render(request,'homeapp/about.html',context)

def contact(request):
    context={'title':'Contact'}
    return render(request,'homeapp/contact.html',context)
