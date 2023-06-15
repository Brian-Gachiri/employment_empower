import json

from django import template
from django.urls import reverse

from backend.models import Membership

register = template.Library()

def range_times(number):
    return range(1, number+1)

def url_value(value):
    return reverse(value)

def jsonify(data):
    if isinstance(data, dict):
        return data
    else:
        return json.loads(data)

def getMembershipName(data):
    ships = data.split(',')
    memberships = Membership.objects.filter(pk__in=ships).values('name')
    return memberships


register.filter('range_times', range_times)
register.filter('url_value', url_value)
register.filter('jsonify', jsonify)
register.filter('memberships', getMembershipName)
