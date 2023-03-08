from django.http import HttpRequest, JsonResponse
import json
from .models import SmartPhone


def add_product(reqeust: HttpRequest) -> JsonResponse:
    """add new product to database"""
    if reqeust.method == 'POST':
        # get body from request
        body = reqeust.body
        # get body data
        decoded = body.decode()
        # data to dict
        data = json.loads(decoded)
        # get all properties
        price = data.get('price', False)
        img_url = data.get('img_url', False)
        color = data.get('color', False)
        ram = data.get('ram', False)
        memory = data.get('memory', False)
        name = data.get('name', False)
        model = data.get('model', False)

        # check all properties is valid
        if price == False:
            return JsonResponse({"status": "price field is required."})
        if img_url == False:
            return JsonResponse({"status": "img_url field is required."})
        if color == False:
            return JsonResponse({"status": "color field is required."})
        if ram == False:
            return JsonResponse({"status": "ram field is required."})
        if memory == False:
            return JsonResponse({"status": "memory field is required."})
        if name == False:
            return JsonResponse({"status": "name field is required."})
        if model == False:
            return JsonResponse({"status": "model field is required."})

        # create a inctance of SmartPhone 
        smartphone = SmartPhone(
            price=price,
            img_url=img_url,
            color=color,
            ram=ram,
            memory=memory,
            name=name,
            model=model
        )
        # save data
        smartphone.save()

        # return data
        returned = smartphone.to_dict()
        return JsonResponse(returned)
    

def get_all_product(reqeust: HttpRequest) -> JsonResponse:
    """get products to database"""
    if reqeust.method == "GET":
        # get all priduct from database
        products = SmartPhone.objects.all()
        # results data
        result = []
        for product in products:
            # add smartphone data as dict
            result.append(product.to_dict())
        
        return JsonResponse(result, safe=False)