from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db import models

from django.template import loader
from django.http import HttpResponse
from django.conf import settings

from mysite.settings import RIOT_SECRET_KEY

import requests
# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    api_url = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
    league_url = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/"
    default_summoner_name = 'hide on bush'
    id_req = requests.get(api_url + default_summoner_name + '?api_key=' + RIOT_SECRET_KEY)
    id = id_req.json()['id']
    info_req = requests.get(league_url + id + '?api_key=' + RIOT_SECRET_KEY)
    info = info_req.json()[0]
    context = {
        'summonerName': info['summonerName'],
        'tier': info['tier']
    }
    
    return HttpResponse(template.render(context, request))
