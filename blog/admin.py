from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from django.utils.translation import ugettext_lazy as _
from blog.models import Blog



#Blog Admin Starts Here
class BlogResource(resources.ModelResource):
    title = fields.Field(column_name=_('Blog Title'), attribute='title')
    description = fields.Field(column_name=_('Description'), attribute='description')
    date = fields.Field(column_name=_('Date'), attribute='date')
    
    class Meta:
        model = Blog
        fields = ('title','description','date')
        import_id_fields = fields
        export_order = fields
    
class BlogAdmin(ImportExportModelAdmin):
    resource_class = BlogResource
    list_display = ('title','short_description','date')
    search_fields = ('title','description','date')
    list_filter = ('title','date',)
#Blog Admin Ends Here

# Register your models here.
admin.site.register(Blog, BlogAdmin)