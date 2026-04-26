import json

from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from .models import Product

# Create your views here.


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "products/index.html", {"products": products})

    def post(self, request):
        try:
            data = json.loads(request.body)
            product = Product.objects.create(
                name=data["name"],
                description=data["description"],
                type=data["type"],
                price=data["price"],
                expiration_date=data["expiration_date"],
            )
            product.save()
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        return JsonResponse({}, status=201)


def create(request):
    return render(request, "products/create.html")
