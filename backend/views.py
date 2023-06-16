import datetime

from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import JsonResponse, HttpResponseRedirect
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
        membership.deleted_at = datetime.datetime.now()
        membership.save()

    data = {
        'success': True
    }
    return JsonResponse(data)

def membership_restore(request, id):
    membership = Membership.objects.filter(id=id).first()
    if membership:
        membership.deleted_at = None
        membership.save()

    data = {
        'success': True
    }
    return JsonResponse(data)

def job_seekers(request):
    clients = Client.objects.all().order_by('-id')

    return render(request, 'job_seekers.html', {'clients': clients})

def job_seeker_detail(request, id):
    client = Client.objects.filter(id=id).first()
    sessions = PrivateSession.objects.filter(client=client).order_by('-id')

    data = {
        'client': client,
        'sessions': sessions
    }
    return render(request, 'seeker_details.html', data)

def content(request):
    contents = Content.objects.all()

    return render(request, 'content.html', {'contents':contents})

def content_details(request, id):
    item = Content.objects.filter(id=id)
    return render(request, 'content_details.html', {'content': item})

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

def create_blog(request):

    if request.method == "GET":
        data = Membership.objects.all()
        return render(request, "blog_create.html", {'memberships': data})

    else:
        name = request.POST.get("title")
        description = request.POST.get("post")
        image = request.FILES.get("image", None)
        tiers = request.POST.getlist('tier[]')
        tier_string = ','.join(tiers)

        Content.objects.create(
            name=name,
            description=description,
            file=image,
            type=Content.BLOG,
            url="https://stuff.com",
            tier_access=tier_string
        )

        return HttpResponseRedirect("/staff/content")

def update_blog(request, id):

    try:
        content = Content.objects.get(pk=id)
    except Content.DoesNotExist:
        return redirectBack(request)

    if request.method == "GET":
        data = Membership.objects.all()
        can_edit = False
        if request.user is content.instructor or request.user.is_superuser:
            can_edit = True
        data = {
            "article": content,
            "can_edit": can_edit,
            'memberships': data
        }
        return render(request, "blog_create.html", data)

    else:
        print(request.POST)
        name = request.POST.get("title")
        description = request.POST.get("post")
        image = request.FILES.get("image", None)
        tiers = request.POST.getlist('tier[]')
        tier_string = ','.join(tiers)

        content.name = name
        content.description =description
        if image:
            content.file = image
        content.tier_access = tier_string
        content.save()


        message = "Blog published successfully."

        messages.info(request, message)
        return HttpResponseRedirect("/staff/content")


def delete_blog(request):
    content = Content.objects.filter(pk=request.POST.get("article")).first()
    if content:
        content.comment_set.all().delete()
        content.delete()

    return HttpResponseRedirect("/staff/content")

def redirectBack(request):
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
