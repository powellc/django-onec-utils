from setuptools import setup, find_packages

setup(
    name='django-markup-mixin',
    version=__import__('markup_mixin').__version__,
    license="BSD",

    install_requires = [],

    description='Add pre-rendered markup fields to your django models with the least work.',
    long_description=open('README.md').read(),

    author='Colin Powell',
    author_email='colin@onecardinal.com',

    url='http://github.com/powellc/django-markup-mixin',
    download_url='http://github.com/powellc/django-markup-mixin/downloads',

    include_package_data=True,

    packages=['markup_mixin'],

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
