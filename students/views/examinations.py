# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.groups import Group
from ..models.examinations import Examination

import pdb

def examinations_add(request):
 	return HttpResponse('<h1>Examination Add Form</h1>')
def examinations_edit(request, sid):
 	return HttpResponse('<h1>Edit Examination%s</h1>' % gid)
def examinations_delete(request, sid):
 	return HttpResponse('<h1>Delete Exception(" error")%s</h1>' % gid)			


def examinations_list(request):
	examinations = Examination.objects.all()
	




	# paginator = Paginator(examinations, 3)
	# page = request.GET.get('page')
	# try:
	# 	examinations = paginator.page(page)
	# except PageNotAnInteger:
	# 	examinations = paginator.page(1)
	# except EmptyPage:
	
	# 	#If page is out of range
	#     #last page of results
	#     examinations = paginator.page(paginator.num_pages) 





	# return render (request, 'students/examinations.html',{'items': examinations})    

	return render(request,'students/examinations.html',
		      {'students': examinations})
