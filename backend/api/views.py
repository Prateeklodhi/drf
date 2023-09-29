from django.shortcuts import render
import json
from django.http import JsonResponse

# Create your views here.
def api_home(request,*args,**kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
        print(data)
    except:
        pass
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type
    print(body)
    return JsonResponse(data)