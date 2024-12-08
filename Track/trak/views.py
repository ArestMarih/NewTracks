
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.forms.models import model_to_dict
from django.http import JsonResponse
from trak.models import quest, Persons, NowExp, Finance, CatFin
from bs4 import BeautifulSoup
import requests
import json
def main(request): # подгрузка всех данных на странцу 
    quests = quest.objects.all()
    user = Persons.objects.all()
    expes = NowExp.objects.all()
    finc = CatFin.objects.all()
    fin = Finance.objects.all()
    return render(request,'trak/main.html',{'data':{'quests':quests,'person':user,'expes':expes,'finc':finc,'fin':fin}})
    
def deleters(request,id): # удаление квеста
        Quest = quest.objects.get(id=id)
        Quest.delete()
        return HttpResponseRedirect('/')

def Poster(request):
    if request.method == "POST":
        nameQu = request.POST.get('nameQu')
        comments = request.POST.get('comments')
        exp = request.POST.get('exp')
        quest.objects.create(nameQu=nameQu, comments=comments, exp=exp)
    return HttpResponseRedirect('/')
 
def done(request,id,exp):  #отмета о выполнении 
    dones = quest.objects.get(id=id)
    dones.done = True
    dones.save()
    plas = NowExp.objects.get(id=1)
    plas.expe = int(plas.expe) + int(exp)
    plas.save()
    return HttpResponseRedirect('/')

def notDone(request,id,exp):
    dones = quest.objects.get(id=id)
    dones.done = False
    dones.save()
    plas = NowExp.objects.get(id=1)
    plas.expe = int(plas.expe) - int(exp)
    plas.save()
    return HttpResponseRedirect('/')
     
     
def edit(request, id):  # удаление квеста 
     p = quest.objects.get(id=id)
     if request.method == "POST":
         p.nameQu = request.POST.get('nameQu')
         p.comments = request.POST.get('comments')
         p.exp = request.POST.get('exp')
         p.save()
         return HttpResponseRedirect('/')

def getQ(request, pk): # получение определенной квест 
     q = quest.objects.filter(id=pk).values()
     return JsonResponse({'q':list(q)})

def AddFinance(request,id):   
    if request.method == "POST":
        namef = request.POST.get('nameF')
        desc = request.POST.get('desc')
        global Income
        Income = request.POST.get('Income')
        count = request.POST.get('count')
        Finance.objects.create(nameF=namef,desc=desc,Income=Income,count=count,category_id=id)
        if Income == "True":
            plas = NowExp.objects.get(id=1)
            plas.Total_money = int(plas.Total_money) + int(count)
            plas.save()
        else:
            plas = NowExp.objects.get(id=1)
            plas.Total_money = int(plas.Total_money) - int(count)
            plas.save()
        return HttpResponseRedirect('/')


def AddCat(request):
    if request.method == "POST":
        Cat = request.POST.get('Cat')      
        CatFin.objects.create(Cat=Cat)
    return HttpResponseRedirect('/')

def coinC(request):
    if request.method == "POST":
        global coin, wallet
        coin = request.POST.get('coin')
        wallet = request.POST.get('wallet')

    url = "https://api.coingecko.com/api/v3/coins/markets?x_cg_demo_api_key=CG-r1umQzviBjg5aMeDfVcjvbjr"
    params={f'ids': '{coin}',
            'vs_currency': '{wallet}'}
    res = requests.get(url, params=params)
    resu = res.json()
    for data in resu:
        resut = [{
        "name": data["id"],
        "price": data["current_price"]
    }]

def test(request):
    url = "https://api.coingecko.com/api/v3/coins/markets?x_cg_demo_api_key=CG-r1umQzviBjg5aMeDfVcjvbjr"
    params={'ids': 'bitcoin',
            'vs_currency': 'usd'}
    res = requests.get(url, params=params)
    resu = res.json()
    for data in resu:
        resut = [{
        "name": data["id"],
        "price": data["current_price"]
    }]
    return render(request, 'trak/test.html', {"res":resut})
