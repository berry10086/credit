from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from mysite.credits.models import Student,Logdate
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.core.context_processors import csrf
import decimal
import re

	
def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
	error = 0
	try:
		student = Student.objects.get(ID = q)
		ID = q
		running = student.running
		match = student.match
		club = student.club
		others = student.others
		credit = student.calcredit()
	except Student.DoesNotExist:
		error =1

	return render_to_response('search_result.html',locals())
#@login_required
def upload_form(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/admin/')
	c = {}
	c.update(csrf(request))
	return render_to_response('upload_form.html',c)
def file_process(request):
	file_obj = request.FILES.get("rawfile", None)
#	[log_date, filetype] = str(file_obj.name()).split('.')
	name = str(file_obj.name)
	[log_date, filetype] = name.split('.')
	if(filetype != 'csv'):
		return HttpResponse('csv only')
	if not re.match("\d{4}-\d{2}-\d{2}",log_date):
		return HttpResponse('filename error!')
	if Logdate.objects.filter(logdate = log_date):
		return HttpResponse('already uploaded!')
	p = Logdate(logdate = log_date)
	p.save()
	filecontext = file_obj.read()
	filecontext = filecontext.split('\n')
	ID_list = []
	
	for line in filecontext:
		line = line.split(',')
		if len(line) == 4 and line[2] == 'STOP_RUNNING':
			ID_list.append(line[1])
	for a in ID_list:
		try:
			p = Student.objects.get(ID = a)
		except Student.DoesNotExist:
			p = Student(ID = a)
			p.save()
		finally:
			p = Student.objects.get(ID = a)
		p.running = p.running + decimal.Decimal(1.5)
		p.save()
	html = 'ok'
	return HttpResponse(html)


