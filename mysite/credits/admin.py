# -*- coding: utf-8 -*-
from django.contrib import admin
from mysite.credits.models import Student,Config

def runningadd(modeladmin, request, queryset):
    step = Config.objects.get(ID = '1').running
    for item in queryset:
    	item.running = item.running + step
    	item.save()
runningadd.short_description = "长跑积分增加 %.1f" % Config.objects.get(ID = '1').running
def matchadd(modeladmin, request, queryset):
    step = Config.objects.get(ID = '1').match
    for item in queryset:
    	item.match = item.match + step
    	item.save()
matchadd.short_description = "赛事积分增加 %.1f" % Config.objects.get(ID = '1').match
def clubadd(modeladmin, request, queryset):
    step = Config.objects.get(ID = '1').club
    for item in queryset:
    	item.club = item.club + step
    	item.save()
clubadd.short_description = "俱乐部积分增加 %.1f" % Config.objects.get(ID = '1').club
def othersadd(modeladmin, request, queryset):
    step = Config.objects.get(ID = '1').others
    for item in queryset:
    	item.others = item.others + step
    	item.save()
othersadd.short_description = "其他积分增加 %.1f" % Config.objects.get(ID = '1').others

#admin.site.disable_action('delete_selected')
class StudentAdmin(admin.ModelAdmin):
    search_fields = ( 'ID', )
    list_display = ('ID','running', 'match', 'club', 'others')
    actions = [runningadd,matchadd,clubadd,othersadd]
    def get_actions(self, request):
    	actions = super(StudentAdmin, self).get_actions(request)
        if request.user.username !=	'sadmin':
            if 'delete_selected' in actions:
            	del actions['delete_selected']
        return actions


class ConfigAdmin(admin.ModelAdmin):
	list_display = ('running', 'match', 'club', 'others')
	def get_actions(self, request):
		actions = super(ConfigAdmin, self).get_actions(request)
		if request.user.username !=	'sadmin':
			if 'delete_selected' in actions:
				del actions['delete_selected']
		return actions    
admin.site.register(Student,StudentAdmin)
admin.site.register(Config,ConfigAdmin)


