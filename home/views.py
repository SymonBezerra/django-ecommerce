import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.http import require_POST

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


@require_POST
def logout_view(request):
    logout(request)
    return JsonResponse({}, status=200)


@login_required(login_url="/login/")
def index(request):
    return render(request, "home/index.html")
