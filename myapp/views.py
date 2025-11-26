from django.shortcuts import render, redirect

from myapp.models import Contact


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

#def 404(request):
    return render(request, '404.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        query = Contact(name=name, email=email, subject=subject, message=message)
        query.save()
        return redirect("/")
    return render(request, 'contact.html')

def donation(request):
    return render(request, 'donation.html')

def event(request):
    return render(request, 'event.html')

def service(request):
    return render(request,'service.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request,'testimonial.html')

def feature(request):
    return render(request, 'feature.html')