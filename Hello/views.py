from django.shortcuts import render
from django.http import HttpResponse
from university.models import ContactUs
# Create your views here.

def world(request,pageid):
	if pageid == "0":
		return HttpResponse("safhe shomare sefr")
	else:
		return HttpResponse("404")


def form(request):
	return render(request,'index.html',{})


def sent(request):
	user_entered_name = request.POST.get('name','noname')
	user_entered_text = request.POST.get('subject','notext')
	this_form = ContactUs(name=user_entered_name,text=user_entered_text)
	this_form.save()
	return render(request,'sent.html',{
		'name':user_entered_name
	})

def messages(request):
	return render(request,'messages.html',{
		'count':ContactUs.objects.count(),
		'messages':ContactUs.objects.all()
	})