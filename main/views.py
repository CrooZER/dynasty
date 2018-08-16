from django.shortcuts import render
from main.mfl import MFL
import json
from django.core import serializers

from . import mfl

# Create your views here.


def index(request):
    return render(request, 'index.html')

def managers(request):
    league = MFL().get_league()
    league = json.loads(league)
    return render(request, 'managers.html', locals())

def franchise(request, id):
    roster = MFL.rosters(id)
    return render(request, 'franchise.html', locals())