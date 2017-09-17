from django import template
from rango.models import Category

register = template.Library()
@register.inclusion_tag('rang/cats.html')
def get_category_list():
    return {'cats': Category.objects.all()}
