# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.


class Examination(models.Model):
	"""Examination Model"""
	
	
	title_exam = models.CharField(
		max_length = 256,
		blank =False,
		verbose_name=u"Название предмета")	


	

	during_time  = models.DateTimeField(
		blank=False,
		verbose_name=u"Время сдачи",
		null=True)


	teacher = models.CharField(
		max_length = 256,
		blank = True,
		verbose_name=u"Преподователь",
		) 

	group = models.ForeignKey('Group',
		null =True,
		blank = True,
		verbose_name=u"Группа",
		
		on_delete = models.SET_NULL
		)


	class Meta(object):
		verbose_name = u"Экзамен"
        verbose_name_plural = u"Экзамен"	

	
	def __unicode__(self):


		if self.teacher:
			return u"%s  %s" % (self.title_exam,  self.group )
		else:
			return u"%s" % title_exam

