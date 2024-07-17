#!/usr/bin/env python3
"""Write strings to Redis"""
import redis

import typing
from uuid import uuid4


data_t = typing.Union[str, bytes, int, float]


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
