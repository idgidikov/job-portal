from django.contrib import admin
from candidates.models import Candidate,CandidateJobMap
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class CandidateResourse(resources.ModelResource):
    class Meta:
        model = Candidate

class CandidateAdmin(ImportExportModelAdmin):
   
    list_display =("name", "mobile","age", "gender", "will_relocate", "city","is_engaged")
    list_filter= ("city", "gender", "will_relocate")
    resources_class = CandidateResourse


class ReviewCandidateAdmin(admin.ModelAdmin):
      list_display =("candidate", "job", "age", "gender", "city", "status")
      list_filter= ("job",)
      list_editable=("status",)
      list_display_links=None

admin.site.register(Candidate, CandidateAdmin)
admin.site.register(CandidateJobMap, ReviewCandidateAdmin)

