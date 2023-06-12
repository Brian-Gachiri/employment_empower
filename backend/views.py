from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from backend.models import Query


def dashboard(request):
    return render(request, 'dashboard.html', {})

def users(request):
    return render(request, 'users.html', {})

def memberships(request):
    return render(request, 'membership_list.html', {})

def job_seekers(request):
    return render(request, 'job_seekers.html', {})

def job_seeker_detail(request):
    return render(request, 'seeker_details.html', {})

def content(request):
    return render(request, 'content.html', {})

def meetings(request):
    return render(request, 'meetings.html', {})

def feedback(request):
    queries = Query.objects.all()
    paginator = Paginator(queries, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'feedback.html', {'queries': page_obj})

def coupons(request):
    return render(request, 'coupons.html', {})

def orders(request):
    return render(request, 'orders.html', {})
