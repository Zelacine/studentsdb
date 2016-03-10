# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.


class Examination(models.Model):
	"""Examination Model"""
	class Meta(object):
		verbose_name = u"Экзамен"
        verbose_name_plural = u"Экзамен"
	
	title = models.CharField(
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

	group = models.OneToOneField('Group',
		null =True,
		blank = True,
		verbose_name=u"Группа",
		on_delete = models.SET_NULL)


	

	def __unicode__(self):

		if self.title:
			return u"%s %s" % (self.title,  self.group)
		else:
			return u"%s" % (self.title)

