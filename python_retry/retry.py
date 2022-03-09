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
    :param retry_on: tuple. Defaults to None.
    :param supress_exception: bool. Defaults to False.
    :param retry_logger: logger.warning(fmt, error, delay) will be called on failed attempts.
        Default: retry.logging_logger. if None, logging is disabled.

    Retry time is calculated as:
        sleep_time = backoff_factor * (2 ** (n_retry - 1))

        n_retry = 1 => backoff_factor * (2 ** (1 - 1))
        n_retry = 2 => backoff_factor * (2 ** (2 - 1))
        n_retry = 3 => backoff_factor * (2 ** (3 - 1))

    Examples:
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
        >>> import logging
        >>> LOGGER = logging.getLogger("foo")
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
        >>> assert not div(1, 0)
        >>>
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
