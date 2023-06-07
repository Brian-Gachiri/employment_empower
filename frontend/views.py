from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'home.html', {})

def contact(request):

    return render(request, 'contact.html', {})

def faq(request):

    return render(request, 'faq.html', {})

def about(request):

    return render(request, 'faq.html', {})

def team(request):

    return render(request, 'faq.html', {})