from django import template

register = template.Library()


@register.filter(name='get')
def get_item(value, item):
    if not value or not item or not isinstance(value, str):
        return None

    attrs = value.split('.')

    for attr in attrs:
        item = getattr(item, attr, None)
        if not item:
            return None
    return item
