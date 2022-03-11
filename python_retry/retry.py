import functools
import logging
import time


logger = logging.getLogger(__name__)


def retry(
    max_retries: int = 3,
    backoff_factor: int = 1,
    retry_on: (Exception,) = None,
    supress_exception: bool = False,
    retry_logger: logging.Logger = None,
):
    """
    Retry decorator

    :param max_retries: int. Defaults to 3.
    :param backoff_factor: int. Defaults to 1.
    :param retry_on: tuple. A tuple of exceptions.
    When no argument is passed all exceptions are catched.
    Defaults to None.
    :param supress_exception: bool. Supress the last exception raised.
    Defaults to False.
    :param retry_logger: logger.warning(fmt, error, delay) will be called on failed attempts.
    Default: retry.logging_logger. if None, logging is disabled.

    The sleep time is calculated as **sleep_time = backoff_factor * (2 ** (n_retry - 1))**.

    Examples:
        >>> from python_retry import retry
        >>> import pytest
        >>> import logging
        >>>
        >>> LOGGER = logging.getLogger("foo")
        >>>
        >>> @retry()
        ... def div(num: int, den: int):
        ...     return num/den
        >>>
        >>> div(1, 0)
        >>>
        >>> @retry(
        ... retry_on=(ZeroDivisionError,),
        ...     max_retries=2,
        ...     backoff_factor=1,
        ...     supress_exception=True,
        ...     retry_logger=LOGGER
        ... )
        ... def div(num: int, den: int):
        ...     return num / den
        >>>
        >>> div(1, 0)
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for n in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except retry_on or Exception as e:
                    # return with/without Exception
                    if n == max_retries:
                        if retry_logger is not None and max_retries:
                            log_str = "%s, retried has been exhausted..."
                            retry_logger.error(log_str, e)
                        if supress_exception:
                            return
                        raise e
                    # time sleep
                    seconds = backoff_factor * (2 ** (n - 1))
                    if retry_logger is not None:
                        log_str = "%s, retrying in %s seconds..."
                        retry_logger.warning(log_str, e, seconds)
                    time.sleep(seconds)

        return wrapper

    return decorator
