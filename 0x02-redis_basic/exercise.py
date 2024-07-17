#!/usr/bin/env python3
"""Write strings to Redis"""
import redis

import typing as t
from uuid import uuid4


data_t = t.Union[str, bytes, int, float]
converter_t = t.Callable


class Cache:
    """Caching system based on redis"""
    def __init__(self) -> None:
        """Creates a connection to redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: data_t) -> str:
        """Store `data` in cache"""
        id = str(uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: t.Optional[converter_t]=None):
        """Get the value of specific key from the cache"""
        res = self._redis.get(key)
        return fn(res) if fn else res

    def get_str(self, key: str):
        return self.get(key, str)

    def get_int(self, key: str):
        return self.get(key, int)
