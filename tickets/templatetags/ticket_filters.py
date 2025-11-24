from django import template

register = template.Library()

@register.filter
def dict_get(dictionary, key):
    """Get an item from a dictionary by key."""
    return dictionary.get(key, [])

@register.filter
def priority_color(score):
    """Return a Bootstrap color class based on priority score."""
    if score >= 80:
        return 'danger'
    elif score >= 60:
        return 'warning'
    elif score >= 40:
        return 'info'
    else:
        return 'secondary'
