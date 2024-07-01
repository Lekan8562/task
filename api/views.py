from django.shortcuts import render
from django.http import JsonResponse

import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import GreetingSerializer

# Create your views here.
@api_view(['GET'])
def hello(request):
    visitor_name = request.GET.get('visitor_name', 'Lekan')
    client_ip = request.META.get('REMOTE_ADDR')
    location = 'Akure'
    temperature = 11
    greeting = f"Hello, {visitor_name}. the temperature is  {temperature} degrees celcius in {location}"

    data = {
        'client_ip':client_ip,
        'location':location,
        'greeting':greeting
    }
    serializer = GreetingSerializer(data)
    return Response(serializer.data)