from django.shortcuts import render, redirect
from requests import Response
from rest_framework.decorators import api_view

# Create your views here.
from .serializers import urlSerializer
from rest_framework.response import Response
from .models import url


@api_view(['POST'])
def url_list(request):
    if request.method == 'POST':
        serializers = urlSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)



def get( request, short_url):
    redirected_url = url.objects.get(short_url=short_url)
    if not redirected_url.url.startswith('http://') and not redirected_url.url.startswith('https://'):
        redirected_url.url = 'https://' + redirected_url.url
    return redirect(redirected_url.url)


