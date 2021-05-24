from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.translation import ugettext_lazy as _


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    date = models.DateField(verbose_name=_("Date"))
    
    @property
    def short_description(self):
        return truncatechars(self.description, 100)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog"
        db_table = 'blog'
        ordering=('title',)
        indexes = [
                models.Index(fields=['title'])
            ]
        
