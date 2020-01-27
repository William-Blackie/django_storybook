from django.conf.urls import url

from .views import compile_dango

django_storybook_urls = [url(r"compile_django/$", compile_dango)]
