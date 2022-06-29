from __future__ import absolute_import, unicode_literals

import os

from setuptools import find_packages, setup

version = __import__('logviewer').__version__


def read(fname):
    # read the contents of a text file
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="django-logviewer",
    version=version,
    url='https://github.com/morlandi/django-logviewer',
    license='BSD',
    platforms=['OS Independent'],
    description="Allows the viewing and download of specific log files in "
                "real time directly from the Django admin interface. ",
    long_description=read('README.md'),
    author='Mario Orlandi',
    author_email='morlandi@brainstorm.it',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Django',
        'Framework :: Django :: 4.0',
        'Programming Language :: Python :: 3.8',
    ],
)
