from django.shortcuts import render, HttpResponseRedirect
from trak.models import quest

def main(request):
    quests = quest.objects.all()
    if request.method == "POST":
        nameQu = request.POST.get('nameQu')
        comments = request.POST.get('comments')
        exp = request.POST.get('exp')
        quest.objects.create(nameQu=nameQu, comments=comments, exp=exp)
    return render(request,'trak/main.html',{'quests':quests})
def deleters(request,id):
        Quest = quest.objects.get(id=id)
        Quest.delete()
        return HttpResponseRedirect('/')