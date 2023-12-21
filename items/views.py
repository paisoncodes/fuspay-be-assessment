from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from items.models import CrudItem
from items.serializers import CrudItemSerializer

class CrudItemAPIView(APIView):
    def get(self, request):
        items = CrudItem.objects.all()
        serializer = CrudItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CrudItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CrudItemDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return CrudItem.objects.get(id=id)
        except CrudItem.DoesNotExist:
            raise Http404

    def get(self, request, id):
        item = self.get_object(id)
        serializer = CrudItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, id):
        item = self.get_object(id)
        serializer = CrudItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        item = self.get_object(id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
