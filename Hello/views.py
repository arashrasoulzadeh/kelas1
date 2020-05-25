from django.shortcuts import render
from django.http import HttpResponse
from university.models import ContactUs,Post,PostCategory,Comment
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



def index(request):
	return render(request,'homepage.html',{
		'posts':Post.objects.all(),
		'categories':PostCategory.objects.all()
	})



def search(request):
	query = request.GET.get('query','')
	return render(request,'search.html',{
		'posts':Post.objects.all().filter(text__contains=query),
		'categories':PostCategory.objects.all()
	})


def page(request,pageid):


	if request.method == 'POST':
		name = request.POST.get('name','no-name')
		text = request.POST.get('text','no-text')
		id = request.POST.get('id')
		comment = Comment(post_id=id,text=text,author=name)
		comment.save()
		pass



	return render(request,'post.html',{
		'post':Post.objects.all().filter(id=pageid)[0],
		'categories':PostCategory.objects.all(),
		'comments':Comment.objects.all().filter(post_id=pageid,is_reviewed=True).order_by('-id')
	})