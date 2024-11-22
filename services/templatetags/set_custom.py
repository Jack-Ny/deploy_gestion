from django import template

register = template.Library()

@register.filter
def set(val=None):
    return val