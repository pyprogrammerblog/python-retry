.. python-retry documentation master file, created by
   sphinx-quickstart on Wed Feb 9 09:57:39 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the Python-Retry documentation!
=================================================

Python retry provides functionality for retrying functions.
It comes with an easy, beautiful and elegant decorator that makes easy to
just decorate any method to be retried.

Features
----------

1. Generic Decorator
2. Specify stop condition (i.e. limit by number of attempts)
3. Specify wait condition (i.e. exponential backoff sleeping between attempts)
4. Customize retrying on Exceptions
5. Logging on retries and exceptions


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   license
   help


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
