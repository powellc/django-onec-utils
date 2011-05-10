from setuptools import setup, find_packages

setup(
    name='django-onec-utils',
    version=__import__('onec_utils').__version__,
    license="BSD",

    install_requires = [],

    description='A collection of misc. tools for One Cardinal\'s work.',
    long_description=open('README.rst').read(),

    author='Colin Powell',
    author_email='colin@onecardinal.com',

    url='http://github.com/powellc/django-onec-utils',
    download_url='http://github.com/powellc/django-onec-utils/downloads',

    include_package_data=True,

    packages=['onec_utils'],

    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
