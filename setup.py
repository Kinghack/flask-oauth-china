"""
Flask-OAuth-China
-----------

Adds OAuth support to Flask.

Links
`````

* `documentation <http://packages.python.org/Flask-OAuth>`_
* `development version
  <http://github.com/mitsuhiko/flask-oauth/zipball/master#egg=Flask-OAuth-dev>`_
"""
from setuptools import setup


setup(
    name='Flask-OAuthChina',
    version='0.1',
    url='https://github.com/Kinghack/flask-oauth-china',
    license='BSD',
    author='happyface',
    author_email='ilsh1022@gmail.com',
    description='Adds OAuth support to Flask in China',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'oauth2',
        'certifi'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
