#coding:utf-8
'''
Created on 2016年2月19日

@author: daelly
'''
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Blog
from sblog.models import Category

categories = Category.objects.all();
choices = (1,)

class BlogForm(forms.ModelForm):
    caption = forms.CharField(label='标题',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}));
    content = forms.CharField(label='内容',widget=CKEditorUploadingWidget());
    category = forms.ChoiceField()
    class Meta:
        fields = ('caption','content');
        model = Blog;
    
class TagForm(forms.Form):
    tag_name = forms.CharField(label='标签',max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}));