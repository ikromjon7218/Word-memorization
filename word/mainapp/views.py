from django.shortcuts import render, redirect
from .models import *

def home_page(request):
    return render(request, "home_page.html")

def essential_english_words(request):
    return render(request, "essential_english_words.html")


def query_essential_1(request):
    if request.method == "POST":
        from_unit = request.POST.get("from_unit"),
        to_unit = request.POST.get("to_unit"),
        amount = request.POST.get("amount"),
        language = request.POST.get("language"),
        return redirect("/test_1_essential/")

    return render(request, "query_essential_1.html")

def test_1_essential(request):
    # random.

    return render(request, "test_1_essential.html")

