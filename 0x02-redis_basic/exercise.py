#!/usr/bin/env python3
"""Write strings to Redis"""
import redis

import typing as t
from functools import wraps
from uuid import uuid4


data_t = t.Union[str, bytes, int, float]
converter_t = t.Callable


def count_calls(method: t.Callable) -> t.Callable:
    """Automaicaly count method's call time"""
    @wraps(method)
    def counter(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return counter


class Cache:
    """Caching system based on redis"""
    def __init__(self) -> None:
        """Creates a connection to redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: data_t) -> str:
        """Store `data` in cache"""
        id = str(uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: t.Optional[converter_t] = None):
        """Get the value of specific key from the cache"""
        res = self._redis.get(key)
        return fn(res) if fn else res

    def get_str(self, key: str):
        return self.get(key, str)

    def get_int(self, key: str):
        return self.get(key, int)

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
