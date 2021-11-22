from django.shortcuts import render

# Create your views here.
def New(request):
    user='john'
    age=25
    number=9526567723
    context={
        'username':user,
        'userage':age,
        'mobile':number,
    }
    return render(request, 'pages/new.html',context)

def Good(request):
    return render(request, 'pages/hello.html')

def Dark(request):
    return render(request, 'pages/up.html') 

def Class(request):
    return render(request, 'pages/class.html') 
       