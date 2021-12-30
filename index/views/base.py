from django.shortcuts import render


def base(request):
    return render(request, "main/base.html")