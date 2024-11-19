from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response

from .models import OrderItem
from .serializer import OrderItemSerializer

class ListCreateOrderItem(generics.ListAPIView):
    queryset = OrderItem.objects.all()  
    serializer_class = OrderItemSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serr = OrderItemSerializer(data=data)
        if (serr.is_valid()):
            serr.save()  
            return Response(serr.validated_data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
