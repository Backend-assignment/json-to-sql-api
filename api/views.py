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