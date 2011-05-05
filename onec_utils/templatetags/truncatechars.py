from django import template

register = template.Library()

@register.filter("truncate")
def truncate(value, size):
    return value[0:size]

@register.filter("truncate_dot")
def truncate_dot(value, size):
    if len(value) > size and size > 3:
        return value[0:(size-3)] + '...'
    else:
        return value[0:size]
