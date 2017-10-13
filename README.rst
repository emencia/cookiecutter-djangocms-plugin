.. _Emencia: http://www.emencia.com/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Django CMS: https://www.django-cms.org/

cookiecutter-djangocms-plugin
=============================

A `Cookiecutter`_ template to produce a basic `Django CMS`_ plugin.

Usage
*****

Just invoke the `Cookiecutter`_ template to create a new project: ::

    cookiecutter https://github.com/emencia/cookiecutter-djangocms-plugin.git

Package content
    Plugin package contains basic structure and files.

Package requirements
    Basic package requirements are ``DjangoCMS`` and ``djangocms-text-ckeditor``.

Naming
    A basic plugin is created with a basic model using capitalized application name
    as model and plugin names, such as:

    * For ``Sample bar`` project name;
    * Package name will be ``cmsplugin-sample-bar``;
    * Application name will ``cmsplugin_sample_bar``;
    * Basic model and plugin names will be ``Samplebar``;

    You can change package and application names during project creation.

Model migrations
    App migrations are not created since shipped model is just a sample and you
    will obviously change it to fit your needs, so you will need to create initial
    migrations once done: ::

        ./manage.py makemigrations ``sample_bar``
