from setuptools import setup, find_packages
 
setup(
    name='django-myutils',
    version='0.1.0',
    description='Just some reusable tools.',
    author='Colin Powell',
    author_email='colin.powell@me.com',
    url='http://github.com/powellc/django-myutils/tree/master',
    packages=find_packages(),
    classifiers=[
        'Development Status :: Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)

