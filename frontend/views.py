from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from backend.models import Query


def home(request):

    return render(request, 'home.html', {})

def contact(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        has_recent_query = Query.objects.filter(email=email).filter(created_at__date=datetime.today()).first()
        if has_recent_query:
            data = {
                'success': False,
                'message': "You have already submitted a query/feedback today"
            }
            return JsonResponse(data)
        Query.objects.create(
            name=name,
            email=email,
            subject=subject,
            text=message
        )
        data = {
            'success': True
        }
        return JsonResponse(data)

    return render(request, 'contact.html', {})

def faq(request):

    return render(request, 'faq.html', {})

def about(request):

    return render(request, 'about.html', {})

def team(request):

    return render(request, 'team.html', {})

def memberships(request):

    return render(request, 'memberships.html', {})