from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from backend.models import *


def dashboard(request):
    plans = Membership.objects.all()
    data = {
        'plans': plans
    }
    return render(request, 'dashboard.html', data)

def users(request):
    return render(request, 'users.html', {})

def memberships(request):
    data = Membership.objects.all().annotate(clients_count=Count('clientmembership'))
    return render(request, 'membership_list.html', {'memberships': data})

def membership_create(request):
    name = request.POST.get('name')
    price = request.POST.get('price')
    tier = request.POST.get('tier')
    description = request.POST.get('description')

    membership_is_present = Membership.objects.filter(Q(name__iexact=name) | Q(tier=tier)).first()
    if membership_is_present:
        data = {
            'success': False,
            'message': 'A membership with a similar name or tier already exists'
        }
        return JsonResponse(data)
    Membership.objects.create(
        name=name,
        price=price,
        tier=tier,
        description=description
    )
    data = {
        'success': True
    }
    return JsonResponse(data)

def membership_delete(request, id):
    membership = Membership.objects.filter(id=id).first()
    if membership:
        membership.delete()

    data = {
        'success': True
    }
    return JsonResponse(data)

def job_seekers(request):
    return render(request, 'job_seekers.html', {})

def job_seeker_detail(request):
    return render(request, 'seeker_details.html', {})

def content(request):
    return render(request, 'content.html', {})

def meetings(request):
    sessions = PrivateSession.objects.all()
    instructors = User.objects.filter(is_staff=True)
    clients = Client.objects.filter(is_active=True)
    data = {
        'meetings': sessions,
        'instructors': instructors,
        'clients': clients
    }
    return render(request, 'meetings.html', data)

def meeting_create(request):
    instructor = request.user
    client = Client.objects.filter(id=request.POST.get('client')).first()
    meeting_url = request.POST.get('url')
    schedule_time = request.POST.get('schedule')

    PrivateSession.objects.create(
        instructor=instructor,
        client=client,
        meeting_url=meeting_url,
        schedule_time=schedule_time
    )
    data = {
        'success': True
    }
    return JsonResponse(data)

def feedback(request):
    queries = Query.objects.all().order_by('-id')
    paginator = Paginator(queries, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'feedback.html', {'queries': page_obj})

def coupon_create(request):
    code = request.POST.get('code')
    expiration = request.POST.get('expiration')
    discount = request.POST.get('discount')
    uses = request.POST.get('uses')

    Coupon.objects.create(
        coupon_code=code,
        coupon_discount=discount,
        expiration_date=expiration,
        maximum_uses=uses,
    )
    data = {
        'success': True
    }
    return JsonResponse(data)

def coupons(request):
    data = Coupon.objects.all().order_by('-id')
    return render(request, 'coupons.html', {'coupons': data})

def orders(request):
    return render(request, 'orders.html', {})
