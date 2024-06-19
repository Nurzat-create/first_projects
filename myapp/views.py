from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.shortcuts import render
from .models import *

# Create your views here.

chab=[{'title':'Главная', 'url_name':'home'},
      {'title':'Меню', 'url_name':'menu'},
      {'title':'О нас', 'url_name':'AboutUs'},
      {'title':'Бронь', 'url_name':'rent'},
    #   {'title:':'Заказ столика', 'url_name':'zakaz'},
      
      
      
      ]



def home(request):
    all_posts=Posts.objects.all()
    all_category=category.objects.all()
    return render(request, 'home.html',{'chab':chab, 'all_category':all_category, 'all_posts':all_posts})


def menu(request):
    all_posts=Posts.objects.all()
    all_category=category.objects.all()
    return render(request, 'menu.html',{'chab':chab, 'all_category':all_category,'all_posts':all_posts})
    
def About(request):
    all_posts=Posts.objects.all()
    all_category = category.objects.all()
    return render(request, 'AboutUs.html', {'chab':chab,'all_posts':all_posts,'all_category': all_category})

def rent(request):
    return render(request, 'rent.html')

from django.shortcuts import render, get_object_or_404

def show_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    all_category=category.objects.all()
    return render(request, 'posts.html',{'chab':chab,'post':post,'all_category':all_category})


def show_category(request, category_id):
    # return HttpResponse(f"Категория под номером {category_id}")

    all_posts = Posts.objects.filter(category_id=category_id)
    all_category = category.objects.all()
    return render(request, 'category.html', {'chab':chab,'title': 'Главная страница', 'menu': menu, 'all_posts': all_posts, 'all_category': all_category})