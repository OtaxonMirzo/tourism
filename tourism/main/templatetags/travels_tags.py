from django import template
from ..models import Region


register = template.Library()

@register.simple_tag(name='get_list_regions')
def get_regions():
    return Region.objects.all()

@register.inclusion_tag('travels/list_regions.html')
def show_regions():
    regions = Region.objects.all()
    return {'regions': regions}
