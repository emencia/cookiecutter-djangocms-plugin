.. _DjangoCMS: https://www.django-cms.org/
.. _djangocms-text-ckeditor: https://github.com/divio/djangocms-text-ckeditor

{{ cookiecutter.project_name }}
{{ '=' * cookiecutter.project_name|length }}

A `DjangoCMS`_ plugin.

Requires
********
* `DjangoCMS`_;
* `djangocms-text-ckeditor`_;

Install
*******

First install package ::

    pip install {{ cookiecutter.package_name }}

Add it to your installed Django apps in settings like this : ::

    INSTALLED_APPS = (
        ...
        'cms',
        ...
        '{{ cookiecutter.app_name }}',
        ...
    )
