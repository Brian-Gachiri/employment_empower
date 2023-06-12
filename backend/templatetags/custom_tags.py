from django import template

register = template.Library()

def range_times(number):
    return range(1, number+1)


register.filter('range_times', range_times)

