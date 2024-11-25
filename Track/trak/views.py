
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.forms.models import model_to_dict
from django.http import JsonResponse
from trak.models import Lvls, quest, Persona

def main(request): # подгрузка всех данных на странцу 
    quests = quest.objects.all()
    user = Persona.objects.all()
    lvl = Lvls.objects.all()
    print(user)
    return render(request,'trak/main.html',{'data':{'quests':quests,'person':user,'lvl':lvl}})
    
def deleters(request,id): # удаление квеста
        Quest = quest.objects.get(id=id)
        Quest.delete()
        return HttpResponseRedirect('/')

def Poster(request): # создание квеста
    if request.method == "POST":
        nameQu = request.POST.get('nameQu')
        comments = request.POST.get('comments')
        exp = request.POST.get('exp')
        quest.objects.create(nameQu=nameQu, comments=comments, exp=exp)
    return HttpResponseRedirect('/')
 
def done(request,id):  #отмета о выполнении 
    dones = quest.objects.get(id=id)
    dones.done = True
    dones.save()
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


