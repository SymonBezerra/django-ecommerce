import json

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

# Create your views here.


class LoginView(View):
    def get(self, request):
        return render(request, "home/login.html")

    def post(self, request):
        data = json.loads(request.body)

        user = authenticate(
            request, username=data["username"], password=data["password"]
        )

        if user:
            try:
                login(request, user)
                return JsonResponse({}, status=200)
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)
        else:
            return JsonResponse({"error": "Invalid username or password"}, status=400)


def index(request):
    return render(request, "home/index.html")
