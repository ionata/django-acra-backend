from acra import VERSION

from setuptools import find_packages, setup


setup(
    name='django-acra-backend',
    version=VERSION,
    description='Django model and admin page for ACRA',
    author='Ionata Digital',
    author_email='webmaster@ionata.com.au',
    url='http://github.com/ionata/django-acra-backend',
    license='BSD',
    packages=find_packages(),
    install_requires=[
        'Django',
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ]
)
