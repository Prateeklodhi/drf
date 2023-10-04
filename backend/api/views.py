from django.shortcuts import render
import json
from django.forms.models import model_to_dict
from product.serializers import ProductSerialier
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import JsonResponse,HttpResponse
from product.models import Product

@api_view(["GET"])
def api_home(request,*args,**kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerialier(instance).data
        # data["id"] = model_data.id
        # data['title'] = model_data.title
        # data["content"] = model_data.content
        # data["price"] = model_data.price
    # json_data_str = json.dumps(data)
    # body = request.body
    # data = {}
    # try:
    #     data['body'] = json.loads(body)
    # except:
    #     pass
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    # print(f"{data['headers']}\n{data['content_type']}")
    return Response(data)
    # return HttpResponse(json_data_str,headers = {"content-type":"application/json"})
    