from django.contrib import admin
from .models import UserEmployee, Education, Experience, AgentManager, Applicant


class UserEmployeeAdmin(admin.ModelAdmin):
    fields = ['username','first_name','last_name', 'mobile_number', 'email',]
    list_display = ('username','first_name','last_name', 'mobile_number', 'email')
    search_fields = ['username']

class  ApplicantAdmin(admin.ModelAdmin):
    fields = ['name', 'fresher_expiriance', 'agent_socialmedia']
    list_display = ['name', 'fresher_expiriance', 'agent_socialmedia']
    search_fiels = ['name', 'fresher_expiriance', 'agent_socialmedia']


class EducationAdmin(admin.ModelAdmin):
    fields = ['name','degree_name','collage_name', 'cgpa']
    list_display = ('name','degree_name','collage_name', 'cgpa')
    search_fields = []


class ExperienceAdmin(admin.ModelAdmin):
    fields = ['name','company_name', 'year_of_experience', 'work', 'domain', 'salary']
    list_display = ('name','company_name', 'year_of_experience', 'work', 'domain', 'salary')
    search_fields = []


class AgentManagerAdmin(admin.ModelAdmin):
    fields = ['username','name', 'code', 'mobile_number', 'post']
    list_display = ('username','name', 'code', 'mobile_number', 'post')
    search_fields = []


admin.site.register(UserEmployee, UserEmployeeAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(AgentManager, AgentManagerAdmin)
admin.site.register(Applicant, ApplicantAdmin)

