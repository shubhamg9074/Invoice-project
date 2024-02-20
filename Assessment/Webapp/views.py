from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse
from .models import Invoice,InvoiceDetail
from .serializers import InvoiceSerializer,InvoiceDetailSerializer

# Create your views here.
class InvoiceList(APIView):
    def get(self,request):
        Invoice1=Invoice.objects.all()
        serializer=InvoiceSerializer(Invoice1,many=True)
        return Response(serializer.data)
    def post(self):
        pass
class InvoiceDetails(APIView):
    def get(self,request):
        invoice=InvoiceDetail.objects.all()
        seializers=InvoiceDetailSerializer(invoice,many=True)
        return Response(seializers.data)
