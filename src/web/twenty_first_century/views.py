from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class ScrapyView(APIView):

    def put(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)
