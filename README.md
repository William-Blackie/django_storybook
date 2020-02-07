# django-storybook
A Django module to intergrate the Storybook pattern library and django

## Installation
```
    pip install django-storybook && pip install django-cors-headers
```

Follow the setup for django-cors-headers [here.](https://github.com/adamchainz/django-cors-headers)

## Config
### Settings.dev
Please note django_storybook disables CSRF protection to allow for local development using Docker. This should not be used in production.

```
    # Enable django_storybook
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_HEADERS = default_headers + ("Access-Control-Allow-Origin", "csrftoken")
```
### Installed apps
Add the following to your installed apps:

```
INSTALLED_APPS =[
    ...
    "django_storybook",
    "corsheaders",
    ...
]
```
### URLs
Add the following to your debug urls:

```
    if settings.debug:
            urlpatterns += url(r"", include(django_storybook_urls)),
```

### Storybook
Add the following to your webpack.config.js:

```
        "django-storybook": "start-storybook -p 6006 & webpack --mode development --progress --watch",
```

While your development environment is running:

```
    npm run django-storybook
```

## Templating
To render django templates, template tags and pass in context you simply import the base template and create props that mimic the expected context. The template variable is the relative path to you desired template.

```
    import React from 'react';
    import BaseTemplate from '../../../../../django_storybook/static_src/js/base-template.js';

    // Set storybook title
    export default { title: 'Card' };

    // Create props for context
    var props = {
        template: 'components/atoms/card/card.html',
        context: {
            card: {
                description: "A super cool company I've worked with",
                url: "https://wwww.google.com",
                button_title: "Vist website"
                },
            card_image: {
            url: "https://via.placeholder.com/250x150?text=William+Blackie"
            }
        },
    }


    // Export 
    export const card = () => (
        <BaseTemplate {...props}/>

    )
```

## Deployment
Due to disabling CSRF django_storybook is not safe for production. However, deploying a static storybook using [storybook deployer](https://github.com/storybookjs/storybook-deployer) is a good alternative.