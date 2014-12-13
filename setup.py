#!/usr/bin/env python

from setuptools import setup, find_packages

about = {}
with open("skylines/__about__.py") as fp:
    exec(fp.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__summary__'],
    author=about['__author__'],
    author_email=about['__email__'],
    url=about['__uri__'],
    packages=find_packages(),
    install_requires=[
         # Packages with a package name behind are available in debian jessie.
         # Their version should not be changed unless the debian package
         # version has changed.
        'flask==0.10.1', # python-flask
        'werkzeug==0.9.6', # python-werkzeug
        'Flask-Babel==0.9', # python-flask-babel
        'Flask-Assets==0.8',
        'Flask-Login==0.2.6', # python-flask-login
        'Flask-Cache==0.12',
        'Flask-Migrate==1.2.0', # python-flask-migrate
        'Flask-Script==0.6.7', # python-flask-script
        'Flask-SQLAlchemy==1.0', # python-flask-sqlalchemy
        'Flask-WTF==0.10.2', # python-flaskext.wtf
        'sqlalchemy==0.9.8', # python-sqlalchemy
        'alembic==0.6.5', # python-alembic
        'psycopg2==2.5.4', # python-psycopg2
        'GeoAlchemy2==0.2.3',
        'Shapely==1.4.3', # python-shapely
        'crcmod==1.7', # python-crcmod
        'Markdown==2.5.1', # python-markdown
        'pytz', # python-tz
        'webassets==0.10.1', # python-webassets
        'cssmin==0.2', # cssmin
        'closure==20140110',
        'WebHelpers==1.3', # python-webhelpers
        'celery[redis]==3.1.13', # python-celery, python-redis
        'xcsoar==0.4',
        'Pygments==2.0.1', # python-pygments
        'aerofiles==0.1.1',
        'enum34==1.0.3', # python-enum34
        'pyproj==1.8.9', # python-pyproj
        'gevent==1.0.1', # python-gevent
    ],
    include_package_data=True,
    package_data={
        'skylines': [
            'i18n/*/LC_MESSAGES/*.mo',
            'templates/*/*',
            'assets/static/*/*'
        ]
    },
    zip_safe=False
)
