from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Report
from .forms import ReportForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

def index(request):
    return HttpResponse("HELLO WORLD")


def me(request):
	Name=Report.objects.all()
	return render(request,'Airapp/sample.html',{'Name':Name})



def page(request):
    Report_list = Report.objects.all()
    paginator = Paginator(Report_list, 3) # Show 3 contacts per page

    page = request.GET.get('page')

    try:
        su = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        su = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 999), deliver last page of results.
        su = paginator.page(paginator.num_pages)

    return render(request, 'Airapp/sample.html', {'su': su})