import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import Context, loader
import json

def home(request):
    return render(request, "myproject/home.html")


def response_viewof_Patient(request):
    url = "https://api-dev.oninnovaccer.com/fhir/Patient?gender=male"
    payload = {}
    headers = {
        "x-api-key": "IwAaqegNrjTRRct1urg3GLeiIAaVjc0w",
        "Content-Type": "application/json",
        "Authorization": "Bearer IwAaqegNrjTRRct1urg3GLeiIAaVjc0w",
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    response = response.json()
    #return JsonResponse(response, safe=False)
    json_pretty = json.dumps(response, sort_keys=True, indent=4)
    return HttpResponse(json_pretty,content_type="application/json")


def response_viewof_RelatedPatient(request):
    url = "https://api-dev.oninnovaccer.com/fhir/RelatedPerson?gender=male"

    payload = {}
    headers = {
        "x-api-key": "IwAaqegNrjTRRct1urg3GLeiIAaVjc0w",
        "Content-Type": "application/json",
        "Authorization": "Bearer IwAaqegNrjTRRct1urg3GLeiIAaVjc0w",
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()
    #json_data = r.json()
    json_pretty = json.dumps(response, sort_keys=True, indent=4)
    return HttpResponse(json_pretty,content_type="application/json")
    #return JsonResponse(response, safe=False)
