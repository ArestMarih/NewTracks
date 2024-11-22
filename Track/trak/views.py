from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from trak.models import quest

def main(request):
    quests = quest.objects.all()
    return render(request,'trak/main.html',{'quests':quests})
    
def deleters(request,id):
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
     return HttpResponseRedirect('/', {'q':q})
