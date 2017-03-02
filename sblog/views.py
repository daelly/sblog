#coding:utf8

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from models import Blog
import service
from django.template.defaultfilters import register
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re
from sblog.models import Category

_SKIN_KEY_ = '_SYSTEM_SKIN_NAME_'
skin = service.get_const(_SKIN_KEY_);
page_size = 9;

@register.filter(name='cstrip')
def content_breviary(content,size):
    if not content:
        content = '';
    #替换注释
    content = re.sub(r'<!--(?!-->).*-->', '', content);
    #替换标签
    content = re.sub(r'<.*?>', '', content);
    if content and len(content) > size:
        return content[:size] + "...";
    else:
        return content;
    
#主页
def blog_home(request):
    blogs = service.hot_blogs(5);
    lastest = service.lastest_blogs(8);
    suggestion = service.visit_blogs(8);
    return render(request, skin+'/home.html', {'blogs': blogs, 'lastest': lastest, 'suggestion': suggestion});

#自我介绍
def blog_about(request):
    return render(request, skin+'/about.html', {});

def blog_learn(request):
    return render(request, 'learn.html', {});

def blog_diary(request):
    return render(request, 'diary.html', {'rg': range(6)});

def blog_shuo(request):
    return render(request, 'shuo.html', {});

def blog_album(request):
    lastest = service.lastest_blogs(8);
    suggestion = service.visit_blogs(8);
    return render(request, skin+'/album.html', {'lastest': lastest, 'suggestion': suggestion});

def blog_board(request):
    return render(request, 'board.html', {});

def blog_category(request, category_slug):
    category = Category.objects.get(category_slug=category_slug);
    blog_list = Blog.objects.filter(category__category_slug=category_slug);
    paginator = Paginator(blog_list, page_size);
    lastest = service.lastest_blogs(8);
    suggestion = service.visit_blogs(8);
    page = request.GET.get('page');
    try:
        blogs = paginator.page(page);
    except PageNotAnInteger:
        blogs = paginator.page(1);
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request, skin+'/list.html', {'page': page, 'blogs': blogs, 'category': category, 'lastest': lastest, 'suggestion': suggestion});

def blog_detail(request, blog_id):
    article = get_object_or_404(Blog, pk=blog_id);
    article.visits = article.visits + 1;
    article.save();
    visits = service.visit_blogs(8);
    suggestion = service.hot_blogs(8);
    return render(request, skin+'/blog.html', {'article': article, 'visits': visits, 'suggestion': suggestion});