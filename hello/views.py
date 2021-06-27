from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import urllib
import json
import re
import requests
from bs4 import BeautifulSoup

# Create your views here.
def index(request):
    URL = 'https://ceb.mu/customer-corner/power-outage-information'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    scripts = soup.find_all('script')

    data=scripts[14]
    #print(data)


    result = scripts[14].decode(eventual_encoding='utf-8')
    result1 = result.replace("\/","/")

    #print(result1)

    start =result1.find('{')+1
    end = result1.find('}')
    finaldata = result1[start:end]
    return HttpResponse(finaldata)
    #return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
