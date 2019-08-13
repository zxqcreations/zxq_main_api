from .models import TextCenter
from .serializers import TextCenterSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.


class TextIndex(APIView):

    def get(self, request):
        all_text = TextCenter.objects.order_by('data_time')
        serializer = TextCenterSerializer(all_text, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        return Response(data, status=200)


class TextDetail(APIView):

    def get_data_entity(self, data_series_number):
        try:
            text = TextCenter.objects.get(data_series_number=data_series_number)
            return text
        except TextCenter.DoesNotExist:
            return None

    def get(self, request, data_series_number):
        entity = self.get_data_entity(data_series_number)
        if entity:
            serializer = TextCenterSerializer(entity)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
