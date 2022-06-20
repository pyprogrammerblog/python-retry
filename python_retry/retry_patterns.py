from typing import Union

import abc


class BasePattern:
    def __int__(self, max_retries: int = 3):
        self.max_retries: int = max_retries
        self.current_retry: int = 0

    @abc.abstractmethod
    def next_retry(self):
        pass


class InnmediateRetryPattern(BasePattern):
    def __int__(self, max_retries: int = 3):
        self.max_retries: int = max_retries
        self.current_retry: int = 0

    def next_retry(self):
        pass


class IncrementalIntervalsPattern(BasePattern):
    """"""

    def __int__(self, max_retries: int = 3, interval: int = 3):
        self.max_retries: int = max_retries
        self._n_retries: int = 0
        self.interval = interval

    def next_retry(self):
        return self.interval * self._n_retries


class ExponentialBackoffPattern(BasePattern):
    """"""

    def __int__(self, backoff_factor: int = 2):
        self.backoff_factor = backoff_factor
        self._n_retries = 0

    def next_retry(self):
        return self.backoff_factor * (2 ** (self._n_retries - 1))


class JitterPattern(BasePattern):
    pass


RetryPatterns = Union[
    JitterPattern,
    ExponentialBackoffPattern,
    InnmediateRetryPattern,
    IncrementalIntervalsPattern,
]
