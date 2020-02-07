from distutils.core import setup
setup(
  name = 'django_storybook', 
  packages = ['django_storybook'],   
  version = '0.1',      
  license='MIT',        
  description = 'A Django module integrating Storybook pattern library and Django',   # Give a short description about your library
  author = 'William Blackie',                   
  author_email = 'will@williamblackie.com',      
  url = 'https://github.com/William-Blackie/django_storybook',  
  download_url = 'https://github.com/William-Blackie/django_storybook/archive/v_01.tar.gz',  
  keywords = ['Django', 'Pattern-library', 'Storybook', 'Pattern library'],  
  install_requires=[
            'django-cors-headers==3.2.1',
            'Django>=2.2,<2.3'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',   
    'Intended Audience :: Developers', 
    'Topic :: Software Development',
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3.6',
  ],
)