from django.contrib import admin
from jobs_portal.models import Job
from candidates.models import CandidateJobMap
from django.contrib.auth.models import User

class CandidateInLine(admin.TabularInline):
    model= CandidateJobMap
    def get_readonly_fields(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return []
        else:
            return ("candidate",)

class JobAdmin(admin.ModelAdmin):
    exclude=("creater",)
    list_display=("position_name","creater")
    inlines=(CandidateInLine,)
    def get_queryset(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return Job.objects.all()
        else:
            return Job.objects.filter(creater= request.user)

    def get_list_display(self, request,*args,**kwargs):
        if request.user.is_superuser:
            return ("position_name","creater")
        else:
            return ("position_name",)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.creater = request.user
            obj.save()

admin.site.register(Job, JobAdmin)


