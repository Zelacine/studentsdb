# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


#views for Journal

def  journal_list(request):
	return HttpResponse('<h1>Journal list</h1>')

def journal_list(request):
	journals =(
		{'id':1,
		 'student':u'Ковалик Эдуард' ,
		 'checkbox': '<input type="checkbox">'}	
		)
		
	return render(request,
		      'journal/journal_list.html',
		      {'journals':journals})
	