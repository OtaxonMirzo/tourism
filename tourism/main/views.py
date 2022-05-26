from django.shortcuts import render
from django.views.generic import ListView

from .models import Travel, Region


def index(request):
    travel = Travel.objects.all()
    travels = {
        'travels': travel,
        'title': "Joy nomlari ro'yhati"
    }
    return render(request, 'travels/home.html', travels)


def get_region(request, region_id):
    travels = Travel.objects.filter(region_id=region_id)
    region = Region.objects.get(pk=region_id)
    context = {
        'travels': travels,
        'region': region,
    }
    return render(request, template_name='travels/list_region.html', context=context)