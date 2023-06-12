from django import template
from django.urls import reverse

register = template.Library()

def range_times(number):
    return range(1, number+1)

def url_value(value):
    return reverse(value)

register.filter('range_times', range_times)
register.filter('url_value', url_value)
