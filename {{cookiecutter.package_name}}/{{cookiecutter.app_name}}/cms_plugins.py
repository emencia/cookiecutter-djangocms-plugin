# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from {{ cookiecutter.app_name }}.models import {{ cookiecutter.app_name|capitalize }} as {{ cookiecutter.app_name|capitalize }}PluginModel
from {{ cookiecutter.app_name }}.forms import {{ cookiecutter.app_name|capitalize }}PluginForm


class {{ cookiecutter.app_name|capitalize }}(CMSPluginBase):
    module = '{{ cookiecutter.project_name }}'
    name = "{{ cookiecutter.app_name|capitalize }}"
    model = {{ cookiecutter.app_name|capitalize }}PluginModel
    form = {{ cookiecutter.app_name|capitalize }}PluginForm
    render_template = '{{ cookiecutter.app_name }}/plugin.html'
    cache = True
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'description',
            ),
        }),
        #(_('Media'), {
            #'fields': (
                #('image',),
            #),
        #}),
    )

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


plugin_pool.register_plugin({{ cookiecutter.app_name|capitalize }})
