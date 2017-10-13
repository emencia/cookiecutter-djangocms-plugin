from setuptools import setup, find_packages

setup(
    name='{{ cookiecutter.package_name }}',
    version=__import__('{{ cookiecutter.app_name }}').__version__,
    description=__import__('{{ cookiecutter.app_name }}').__doc__,
    long_description=open('README.rst').read(),
    author='{{ cookiecutter.package_author_name }}',
    author_email='{{ cookiecutter.package_author_email }}',
    url='https://{{ cookiecutter.repo_host }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.package_name }}',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        #'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        "Programming Language :: Python",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'django-cms',
        'djangocms-text-ckeditor',
    ],
    include_package_data=True,
    zip_safe=False
)