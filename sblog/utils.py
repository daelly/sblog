#coding:utf-8
'''
Created on 2016年2月20日

@author: daelly
'''
import re

def content_breviary(content,size):
    if content and len(content) > size:
        return content[:size] + "...";
    else:
        return content;