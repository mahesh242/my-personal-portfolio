from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.translation import ugettext_lazy as _


class Project(models.Model):
    title = models.CharField(max_length=100,verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(upload_to="portfolio/images/",verbose_name=_("Image"))
    url = models.URLField(blank=True,verbose_name=_("Url"))

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Project"
        db_table = 'project'
        ordering=('title',)
        indexes = [
                models.Index(fields=['title'])
            ]
        