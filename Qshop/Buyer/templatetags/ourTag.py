from django import template
register = template.Library()

@register.filter
def uper(obj):
    return obj.upper()

@register.filter
def get_four(obj,i):
    return obj[:int(i)]