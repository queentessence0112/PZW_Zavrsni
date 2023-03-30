from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from .forms import PacijentForm
from .models import Pacijent

# Create your views here.

def pacijent_list(request):
    context = {'pacijent_list':Pacijent.objects.all()}
    return render(request, "main/pacijent_list.html", context)

def pacijent_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PacijentForm()
        else:
            pacijent = Pacijent.objects.get(pk=id)
            form = PacijentForm(instance=pacijent)
        return render(request, "main/pacijent_form.html", {"form":form})
    else:
        if id == 0:
            form = PacijentForm(request.POST)
        else:
            pacijent = Pacijent.objects.get(pk=id)
            form = PacijentForm(request.POST, instance=pacijent)
        if form.is_valid():
            form.save()
        return redirect("/pacijenti/list")

def pacijent_delete(request,id):
    pacijent = Pacijent.objects.get(pk=id)
    pacijent.delete()
    return redirect("/pacijenti/list")


def LoginView(request):
    return HttpResponseRedirect(reverse('login'))