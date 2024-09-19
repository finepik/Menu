from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag
def menu_item(tree, parent_url):
    context = {
        'tree': tree,
        'parent_url': parent_url
    }
    return render_to_string('menuapp/menu-item.html', context=context)
