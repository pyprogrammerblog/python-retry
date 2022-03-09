from python_retry import retry

import logging
import pytest


logger = logging.getLogger(__name__)


def test_method():
    @retry()
    def add(a: int, b: int):
        return sum([a, b])

    assert 4 == add(1, 3)
    assert 5 == add(3, 2)
    assert 10 == add(5, 5)


def test_retry_exceptions(caplog):
    @retry()
    def add(a, b):
        a = int(a)  # if a not numeric then ValueError
        return sum([a, b])  # if b not

    with pytest.raises(TypeError):
        add(a=1, b="1")

    with pytest.raises(ValueError):
        add(a="a", b=1)

    assert caplog.messages == []


def test_retry_specific_exceptions(caplog):
    @retry(
        retry_on=(TypeError, ValueError),
        max_retries=1,
        backoff_factor=1,
        retry_logger=logging.getLogger("foo"),
    )
    def add(a, b):
        a = int(a)  # if a not numeric then ValueError
        return sum([a, b])  # if b not

    log_messages = [
        "unsupported operand type(s) for +: 'int' and 'str', "
        "retrying in 0.5 seconds...",
        "unsupported operand type(s) for +: 'int' and 'str', "
        "retried has been exhausted...",
        "invalid literal for int() with base 10: 'a', "
        "retrying in 0.5 seconds...",
        "invalid literal for int() with base 10: 'a', "
        "retried has been exhausted...",
    ]

    with pytest.raises(TypeError):
        add(a=1, b="1")

    with pytest.raises(ValueError):
        add(a="a", b=1)

    assert caplog.messages == log_messages


def test_retry_all_exceptions(caplog):
    @retry(max_retries=1, backoff_factor=1)
    def add(a, b):
        a = int(a)  # if a not numeric then ValueError
        return sum([a, b])  # if b not

    with pytest.raises(TypeError):
        add(a=1, b="1")

    with pytest.raises(ValueError):
        add(a="a", b=1)

    assert caplog.messages == []


def test_retry_supress_exception(caplog):
    @retry(
        retry_on=(ValueError, TypeError),
        max_retries=1,
        backoff_factor=1,
        supress_exception=True,
        retry_logger=logging.getLogger("foo"),
    )
    def add(a, b):
        a = int(a)  # if a not numeric then ValueError
        return sum([a, b])  # if b not

    log_messages = [
        "unsupported operand type(s) for +: 'int' and 'str', "
        "retrying in 0.5 seconds...",
        "unsupported operand type(s) for +: 'int' and 'str', "
        "retried has been exhausted...",
        "invalid literal for int() with base 10: 'a', "
        "retrying in 0.5 seconds...",
        "invalid literal for int() with base 10: 'a', "
        "retried has been exhausted...",
    ]

    assert not add(a=1, b="1")
    assert not add(a="a", b=1)
    assert caplog.messages == log_messages
