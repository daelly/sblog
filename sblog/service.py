#coding:utf-8
'''
Created on 2017年2月18日

@author: daelly
'''
from sblog.models import Blog, Constanter
from django.core.cache import cache

_constant_key_ = '_constant_key_';

"""
获取首页的前size条博客
"""
def hot_blogs(size):
    blogs = Blog.objects.all()[:size];
    return blogs;

"""
获取浏览量前size条的博客
"""
def visit_blogs(size):
    blogs = Blog.objects.order_by('-visits').all()[:size];
    return blogs;

def lastest_blogs(size):
    blogs = Blog.objects.order_by('-update_time').all()[:size];
    return blogs;

"""
获取所有系统常量
"""
def constanter():
    constants = cache.get(_constant_key_);
    if constants:
        return constants;
    constants = Constanter.objects.all();
    dicct = {};
    for item in constants:
        k = item.the_key;
        v = item.the_value;
        dicct[k] = v;
    cache.set(_constant_key_, dicct);
    return dicct;

"""
获取指定key的系统常量
"""
def get_const(key):
    constants = constanter();
    print constants;
    return constants.get(key);

def reset_cache():
    constants = Constanter.objects.all();
    dicct = {};
    for item in constants:
        k = item.the_key;
        v = item.the_value;
        dicct[k] = v;
    cache.set(_constant_key_, dicct);