from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from django.utils.translation import ugettext_lazy as _
from portfolio.models import Project



#Project Admin Starts Here
class ProjectResource(resources.ModelResource):
    title = fields.Field(column_name=_('Project Title'), attribute='title')
    description = fields.Field(column_name=_('Description'), attribute='description')
    image = fields.Field(column_name=_('Image'), attribute='image')
    url = fields.Field(column_name=_('Url'), attribute='url')
    
    class Meta:
        model = Project
        fields = ('title','description','image','url',)
        import_id_fields = fields
        export_order = fields
    
class ProjectAdmin(ImportExportModelAdmin):
    resource_class = ProjectResource
    list_display = ('title','short_description','image','url',)
    search_fields = ('title','description','image','url',)
    list_filter = ('title','url',)
#Project Admin Ends Here

# Register your models here.
admin.site.register(Project, ProjectAdmin)