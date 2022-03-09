Quickstart
==========

This is a quick introduction with a more advanced example.

Using the Python retry decorator
---------------------------------

.. code:: python

    >>> from python_retry import retry
    >>>
    >>> @retry()
    ... def div(num: int, den: int):
    ...     return num/den
    >>>
    >>> import pytest
    >>> with pytest.raises(TypeError):
    ...     div(1, 0)
    >>>


A more advanced use
--------------------

.. code:: python

    >>> import logging
    >>> logger = logging.getLogger("foo")
    >>> @retry(
    ... retry_on=(ZeroDivisionError,),
    ...     max_retries=2,
    ...     backoff_factor=1,
    ...     supress_exception=True,
    ...     retry_logger=logger
    ... )
    ... def div(num: int, den: int):
    ...     return num / den
    >>>
    >>> assert not div(1, 0)
    >>>
