# -*- coding: utf-8 -*-
from django.db import models
from django import forms

    
class Student(models.Model):
	ID = models.CharField(max_length = 10, primary_key = True, unique = True, verbose_name = u'学号')
	running = models.DecimalField(max_digits = 3, decimal_places = 1 ,default = 0.0, verbose_name = u'长跑')
	match = models.DecimalField(max_digits = 3, decimal_places = 1, default = 0.0, verbose_name = u'赛事')
	club = models.DecimalField(max_digits = 3, decimal_places = 1, default = 0.0, verbose_name = u'俱乐部')
	others = models.DecimalField(max_digits = 3, decimal_places = 1, default = 0.0, verbose_name = u'其他')


	def __unicode__(self):
		return self.ID
	def display(self):
		print 'ID','=>',self.ID
		print 'running','=>',self.running
		print 'match','=>',self.match
		print 'club','=>',self.club
		print 'others','=>',self.others
	def calcredit(self):
		return self.running + self.match + self.club + self.others

class Logdate(models.Model):
	logdate = models.CharField(max_length = 20, primary_key = True, unique = True)

class Config(models.Model):
	ID = models.CharField(max_length = 10, primary_key = True, unique = True) 
	running = models.DecimalField(max_digits = 3, decimal_places = 1 ,default = 1.5, verbose_name = u'长跑')
	match = models.DecimalField(max_digits = 3, decimal_places = 1, default = 1.5, verbose_name = u'赛事')
	club = models.DecimalField(max_digits = 3, decimal_places = 1, default = 1.5, verbose_name = u'俱乐部')
	others = models.DecimalField(max_digits = 3, decimal_places = 1, default = 1.5, verbose_name = u'其他')
