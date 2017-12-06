from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter()
def encode_mailto(text):
    """gugus msut be present in the html header."""
    if "@" not in text:
        return text
    a, b = text.split("@")
    script = "<script type=\"text/javascript\">gugus('%s', '%s', '');</script>"
    return mark_safe(script % (a, b))
