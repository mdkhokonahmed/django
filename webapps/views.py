from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Category, Post, Slider, Logo
# Create your views here.
def index(request):
	all_categoris = Category.objects.raw("SELECT * FROM webapps_category WHERE status='0' ORDER BY id DESC LIMIT 5")
	#all_categoris = Category.objects.all(status='0')
	all_posts = Post.objects.all()
	list_slider = Slider.objects.all()
	list_logo = Logo.objects.all()

	return render(request,'index.html',{'all_categoris':all_categoris, 'all_posts':all_posts, 'list_slider':list_slider,'list_logo':list_logo})

def about(request):
	list_logo = Logo.objects.all()
	return render(request,'about.html', {'list_logo':list_logo})

def contact(request):
	list_logo = Logo.objects.all()
	return render(request,'contact.html', {'list_logo':list_logo})
	
def postlist(request, id):
	list_logo = Logo.objects.all()
	try:
		all_posts = Post.objects.get(pk=id)
	except Post.DoesNotExist:
		raise Http404

	all_categoris = Category.objects.raw("SELECT * FROM webapps_category WHERE status='0' ORDER BY id DESC LIMIT 5")
	#all_posts = get_object_or_404(Post, pk=id)
	return render(request,'postlist.html', {'all_categoris':all_categoris, 'all_posts':all_posts,'list_logo':list_logo})

