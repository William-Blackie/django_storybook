import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'django_storybook', 
  version = '0.1.4',      
  license='MIT',        
  description = 'A Django module integrating Storybook pattern library and Django',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'William Blackie',                   
  author_email = 'contact@williamblackie.com',      
  url = 'https://github.com/William-Blackie/django_storybook',  
  download_url = 'https://github.com/William-Blackie/django_storybook/archive/v_0.1.4.tar.gz',  
  keywords = ['Django', 'Pattern-library', 'Storybook', 'Pattern library'],  
  packages=setuptools.find_packages(),
  classifiers=[
    'Development Status :: 3 - Alpha',   
    'Intended Audience :: Developers', 
    'Topic :: Software Development',
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3.6',
  ],
  python_requires='>=3.6',
)