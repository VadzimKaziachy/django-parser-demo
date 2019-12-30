from django.shortcuts import render

from .services.home_service import HomeService


def index(request):
    home_service = HomeService()
    context = home_service.get_home_page()
    return render(request=request, template_name='home_page.html', context=context)
