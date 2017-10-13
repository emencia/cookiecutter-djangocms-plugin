# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

#from filebrowser.fields import FileBrowseField

from cms.models.pluginmodel import CMSPlugin


class {{ cookiecutter.app_name|capitalize }}(CMSPlugin):
    title = models.CharField(
        _(u"Title"),
        max_length=120,
    )
    #image = FileBrowseField(
        #_('image'),
        #max_length=255,
        #null=True,
        #blank=True,
        #default=None,
    #)
    description = models.TextField(
        _(u"Description"),
        blank=True,
        null=True,
    )

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super({{ cookiecutter.app_name|capitalize }}, self).save(*args, **kwargs)
