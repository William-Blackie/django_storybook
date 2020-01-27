# django-storybook
A Django module to intergrate the Storybook pattern library and django

## Settings.dev
Please note django_storybook disables CSRF protection to allow for local development using Docker. This should not be used in production.

    # Enable django_storybook
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_HEADERS = default_headers + ("Access-Control-Allow-Origin", "csrftoken")

## urls
Add the following to your debug urls:

    if settings.debug:
            urlpatterns += url(r"", include(django_storybook_urls)),
