from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from .forms import BodySerializer
from .tasks import start_handler_product


class ScrapyView(APIView):

    def put(self, request, category_pk=None, *args, **kwargs):
        start_handler_product.delay()
        # print(request.data)
        # data = BodySerializer(data=request.data, many=True)
        # if data.is_valid():
        #     return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_409_CONFLICT)
