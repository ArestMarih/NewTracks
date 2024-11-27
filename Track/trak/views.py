import json
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.forms.models import model_to_dict
from django.http import JsonResponse
from trak.models import Lvlvs, Person, quest

def main(request):
    quests = quest.objects.all()
    return render(request,'trak/main.html',{'data':{'quests':quests,'lvl':Lvlvs,'person':Person}})
    
def deleters(request,id):
        Quest = quest.objects.get(id=id)
        Quest.delete()
        return HttpResponseRedirect('/')

def done(request,id):
    dones = quest.objects.get(id=id)
    dones.done = True
    dones.save()
    return HttpResponseRedirect('/')

def Poster(request):
    if request.method == "POST":
        nameQu = request.POST.get('nameQu')
        comments = request.POST.get('comments')
        exp = request.POST.get('exp')
        quest.objects.create(nameQu=nameQu, comments=comments, exp=exp)
    return HttpResponseRedirect('/')

def edit(request, id):
     p = quest.objects.get(id=id)
     if request.method == "POST":
         p.nameQu = request.POST.get('nameQu')
         p.comments = request.POST.get('comments')
         p.exp = request.POST.get('exp')
         p.save()
         return HttpResponseRedirect('/')


def getQ(request, pk):
     q = quest.objects.filter(id=pk).values()
     return JsonResponse({'q':list(q)})


     