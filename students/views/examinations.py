# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.groups import Group
from ..models.examinations import Examination

import pdb


def students_list(request):
	
 	return render (request, 'students/examinations.html',{})
def examinations_add(request):
 	return HttpResponse('<h1>Examination Add Form</h1>')
def examinations_edit(request, sid):
 	return HttpResponse('<h1>Edit Examination%s</h1>' % gid)
def examinations_delete(request, sid):
 	return HttpResponse('<h1>Delete Exception(" error")%s</h1>' % gid)			

def examinations_list(request):
	examinations = Examination.objects.all()
	examinations = examinations.order_by('title_exam')
	
# pdb.set_trace()
	return render(request,'students/examinations.html',{'examinations': examinations})
