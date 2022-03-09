from django import template
from django.utils import timezone

register = template.Library()


@register.filter
def days_since(last_edit_date):
    delta = timezone.localtime(timezone.now()) - last_edit_date
    return delta.days
