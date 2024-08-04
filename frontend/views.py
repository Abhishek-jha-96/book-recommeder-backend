from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import JsonResponse
import requests


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        response = requests.post(
            "http://localhost:8000/api/v1/token/",
            data={"username": username, "password": password},
        )
        if response.status_code == 200:
            data = response.json()
            request.session["access_token"] = data.get("access")
            request.session["refresh_token"] = data.get("refresh")
            return redirect("book_list")
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=400)
    return render(request, "home.html")


def logout(request):
    request.session.flush()
    return redirect("login")


def book_list(request):
    token = request.session.get('access_token')
    headers = {'Authorization': f'Bearer {token}'} if token else {}
    
    try:
        response = requests.get('http://localhost:8000/api/v1/community/book/', headers=headers)
        response.raise_for_status()
        books = response.json()
        return render(request, 'book_list.html', {'books': books})
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return JsonResponse({'error': 'Failed to fetch books'}, status=500)
    except ValueError as e:
        print(f"JSON decoding failed: {e}")
        return JsonResponse({'error': 'Failed to decode JSON'}, status=500)

