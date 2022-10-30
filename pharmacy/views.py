from django.shortcuts import render,redirect
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.http import response
from .models import Pharmacy
from .forms import PharmacyForm


def index(request):
    list_pharmacy = Pharmacy.objects.all()
    context = { 
        'pharmacy': list_pharmacy,
    }
    return render(request, 'index.html', context, {'list_pharmacy':list_pharmacy})



def create_pharmacy(request):
    if request.method == 'POST':
        form = PharmacyForm(request.POST)
        if form.is_valid:
            pharmacy_form = form.save(commit=False)
            pharmacy_form.save()
            return response.HttpResponseRedirect('/pharmacy')
    else:
        form = PharmacyForm()

    return render(request,'index.html', {'form':form})