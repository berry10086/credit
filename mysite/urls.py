from django.conf.urls import patterns, include, url
from mysite.views import search_form,search,upload_form,file_process
from django.contrib import admin
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	('^$',search_form),
	('^search/$',search),
	url(r'^admin/', include(admin.site.urls)),
	('^upload/$',upload_form),
	('^upload/file/$',file_process),
)
