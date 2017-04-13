from django.shortcuts import render

def _403(request):
    return render(request, '403.html', {})

def _404(request):
    return render(request, '404.html', {})

def _500(request):
    return render(request, '500.html', {})
