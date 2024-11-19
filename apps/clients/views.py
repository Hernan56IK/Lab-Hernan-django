from rest_framework import generics, status
from rest_framework.response import Response

from .models import Customer
from .serializer import CustomerSerializer

class ListCreateClients(generics.ListAPIView):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer
  
  def post(self, request, *args, **kwargs):
    data= request.data
    serr = CustomerSerializer(data=data)
    if (serr.is_valid()):
      serr.save()
      return Response(serr.validated_data, status=status.HTTP_200_OK)  
    
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
