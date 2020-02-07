import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def compile_dango(request):
    data = json.load(request)
    return render(request, data["template"], data["context"])
