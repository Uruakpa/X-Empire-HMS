from django.shortcuts import render


def about_page(request):
    context = {}
    return render(request, "guest/about.html", context)