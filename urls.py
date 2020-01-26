from .views import compile_dango
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

django_storybook_urls = url(r"compile_django/$", compile_dango),

