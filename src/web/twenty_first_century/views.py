from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from .forms import BodySerializer


class ScrapyView(APIView):

    def get(self, request, *args, **kwargs):
        requests.post(url='http://parser:6800/schedule.json?project=twenty_first_century&spider=category&category=https://www.21vek.by/notebooks/')
        return Response(status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        print(request.data)
        data = BodySerializer(data=request.data, many=True)
        if data.is_valid():
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_409_CONFLICT)
