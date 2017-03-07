from setuptools import find_packages, setup


install_requires = [
    'django>=1.8',
]

tests_require = [
    'pytest==3.0.6',
    'pytest-cov==2.4.0',
    'pytest-django==3.1.2',
    'pytest-sugar==0.7.1',
]


setup(
    name='django-cache-results',
    version='0.9',
    description='A microlibrary to ease cache storage and retrieval',
    author='Lab Digital BV',
    author_email='info@labdigital.nl',
    url='https://github.com/LabD/django-cache-results',
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
    },
    license='Apache 2.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    long_description=open('README.rst').read(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
