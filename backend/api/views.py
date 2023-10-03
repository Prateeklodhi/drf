from django.shortcuts import render
import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from product.models import Product
def api_home(request,*args,**kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data)
        # data["id"] = model_data.id
        # data['title'] = model_data.title
        # data["content"] = model_data.content
        # data["price"] = model_data.price

    # body = request.body
    # data = {}
    # try:
    #     data['body'] = json.loads(body)
    # except:
    #     pass
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    # print(f"{data['headers']}\n{data['content_type']}")

    return JsonResponse(data)
    