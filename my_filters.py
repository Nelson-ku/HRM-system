from django import template

register = template.Library()


@register.filter
def minus_date(end_date, start_date):
    d_diff = end_date - start_date

    return 29 - d_diff.days
