# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models.students import Student


def students_list(request):
	
 	return render (request, 'students/students_list.html',{})
def students_add(request):
 	return HttpResponse('<h1>Student Add Form</h1>')
def students_edit(request, sid):
 	return HttpResponse('<h1>Edit Student%s</h1>' % sid)
def students_delete(request, sid):
 	return HttpResponse('<h1>Delete Student%s</h1>' % sid)			



# def students_list(request):
# 	students =(
# 		{'id':1,
# 		 'first_name': u'Віталій',
# 	     'last_name': u'Подоба',
# 	     'ticket': 235,
# 	     'image': 'img/me.jpeg'},
# 		{'id': 2,
# 	     'first_name': u'Корост',
# 	     'last_name': u'Андрій',
# 	     'ticket': 2123,
# 	     'image': 'img/piv.png'},
# 	    {'id': 3,
# 	     'first_name': u'Ковалик',
# 	     'last_name': u'Эдуард',
# 	     'ticket':13,
# 	     'image': 'img/004.jpg'} 
# 		)
def students_list(request):
	students = Student.objects.all()
	students = students.order_by('first_name')

	#TRY TO ORDER students list -- sortirovka
	if request.GET.get('order_by','')=='':
		request.GET.order_by='last_name'
	order_by=request.GET.get('order_by','')
	if order_by in ('id','last_name', 'first_name','ticket'):
		students = students.order_by(order_by)
		if request.GET.get('reverse','') == '1':
			students = students.reverse()
	
	#Paginator students 
	paginator = Paginator(students, 3)
	page = request.GET.get('page')
	try:
		students = paginator.page(page)
	except PageNotAnInteger:
		students = paginator.page(1)
	except EmptyPage:
	
		#If page is out of range
	    #last page of results
	    students = paginator.page(paginator.num_pages) 




	return render(request,
		      'students/students_list.html',
		      {'students':students})