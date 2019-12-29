from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .services.home_service import HomeService


class HomeView(generics.RetrieveAPIView):

    home_service = HomeService()

    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        result = self.home_service.get_home_page()
        return Response(data=result, template_name='home_page.html')

