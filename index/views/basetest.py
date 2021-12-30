from django.shortcuts import render


def basetest(request):
    return render(request, "main/base_test.html")