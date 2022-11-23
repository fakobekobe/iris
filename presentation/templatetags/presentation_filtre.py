from django import template

register = template.Library()

@register.filter
def liste(variable, parametre):
    try:
        return variable[parametre]
    except:
        return ""