from django import template

register = template.Library()

@register.filter
def counters(List):
    return range(len(List))

@register.filter
def index(List, i):
    return List[int(i)]