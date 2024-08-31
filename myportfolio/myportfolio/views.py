from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'landingpage/index.html')

def track(request):
    if request.method == 'POST':
        print("Visitor clicked the button")
        return JsonResponse({'message': 'Button clicked!'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

from .models import Visit

def track(request):
    if request.method == 'POST':
        Visit.objects.create(action='clicked')
        return JsonResponse({'message': 'Button clicked!'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

from django.shortcuts import render

def index(request):
    return render(request, 'landingpage/index.html')

