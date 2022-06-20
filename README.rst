Python Retry
=============

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://github.com/pyprogrammerblog/python-retry/blob/master/LICENSE
    :alt: License-MIT

.. image:: https://readthedocs.org/projects/py-retry/badge/?version=latest
    :target: https://py-retry.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://github.com/pyprogrammerblog/python-retry/workflows/Test%20Suite/badge.svg/
    :alt: GitHub Actions

.. image:: https://badge.fury.io/py/python-retry.svg/
    :target: https://badge.fury.io/py/python-retry/
    :alt: Badge PyPi

.. image:: https://coveralls.io/repos/github/pyprogrammerblog/python-retry/badge.svg?branch=master
    :target: https://coveralls.io/github/pyprogrammerblog/python-retry?branch=master
    :alt: Coverage


Features
----------

1. Generic Decorator
2. Specify stop condition (i.e. limit by number of attempts)
3. Specify wait condition (i.e. exponential backoff sleeping between attempts)
4. Customize retrying on Exceptions

`Read the docs <https://py-retry.readthedocs.io/en/latest/>`_ for further information.

Installation
-------------

Install using ``pip``::

    pip install python-retry


Example
--------

.. code:: python

    >>> from python_retry import retry
    >>> import pytest
    >>>
    >>> @retry()
    ... def div(num: int, den: int):
    ...     return num/den
    >>>
    >>> div(1, 0)


Advanced use
--------------

.. code:: python

    >>> import logging
    >>> logger = logging.getLogger("foo")
    >>>
    >>> @retry(
    ...     retry_on=(ZeroDivisionError,),
    ...     max_retries=2,
    ...     backoff_factor=1,
    ...     supress_exception=True,
    ...     retry_logger=logger
    ... )
    ... def div(num: int, den: int):
    ...     return num / den
    >>>
    >>> div(1, 0)


Documentation
---------------

You can find here at `Read the docs <https://py-retry.readthedocs.io/en/latest/>`_ the complete documentation.
