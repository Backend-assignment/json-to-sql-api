from django.http import HttpRequest, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import json
from .models import SmartPhone


def add_product(reqeust: HttpRequest) -> JsonResponse:
    """add new product to database"""
   
    

def get_all_product(reqeust: HttpRequest) -> JsonResponse:
    """get products to database"""
   
    

def get_product(reqeust: HttpRequest, pk: int) -> JsonResponse:
    """get product from database by id"""


def delete_product(reqeust: HttpRequest, pk: int) -> JsonResponse:
    """delete product from database by id"""
 
    

def update_product(reqeust: HttpRequest, pk: int) -> JsonResponse:
    """delete product from database by id"""
 



