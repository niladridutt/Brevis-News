from django import template

register = template.Library()

@register.filter
def to_plus(value):
    return value.replace(" ","+")