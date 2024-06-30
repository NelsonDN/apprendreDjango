from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name= "first_char")
@stringfilter
def first_char(value):
    return value[0]

@register.filter(name= "lengthis")
def checkstrlen(value, size):
    return len(value) == size

@register.simple_tag
def hello_world(username):
    return f"Hello World {username}!"