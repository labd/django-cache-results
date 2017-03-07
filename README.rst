.. image:: https://img.shields.io/travis/LabD/django-cache-results/master.svg?branch=master
    :target: http://travis-ci.org/LabD/django-cache-results
.. image:: https://img.shields.io/pypi/v/LabD.svg
    :target: https://pypi.python.org/pypi/LabD/
.. image:: https://img.shields.io/pypi/l/LabD.svg
    :target: https://pypi.python.org/pypi/LabD/
.. image:: https://img.shields.io/codecov/c/github/LabD/django-cache-results/master.svg
    :target: https://codecov.io/github/LabD/django-cache-results?branch=master

django-cache-results
======================

A microlibrary to ease your caching code.

Usage:

.. code-block:: python

    def key_function(arg1, arg2):
        return f"prefix.{arg1}.{arg2}"

    @cache_results(key_function=key_function)
    def some_function(arg1, arg2):
        return "COMPLEX DATA"

Normal usage:

.. code-block:: python

    value = some_function(1, 2)

Skipping the cache:

.. code-block:: python

    value = some_function.bypass_cache(1, 2)

Updating the cache:

.. code-block:: python

    value = some_function.refresh_cache(1, 2)

Fetch the key for manual action:

.. code-block:: python

    cache_key = some_function.cache_key(1, 2)


Installation
============

Install the module from PyPI:

.. code-block:: bash

    pip install django-cache-results

And use it in your project:

.. code-block:: python

    from cache_results import cache_results


Contributing
------------

Was there something you missed, or didn't like about this module?
Send us a pull request!


.. _documentation: http://django-cache-results.readthedocs.org/
