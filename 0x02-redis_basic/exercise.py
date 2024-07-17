#!/usr/bin/env python3
"""Using Redis as in-memroy Cache"""
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


def call_history(method: t.Callable) -> t.Callable:
    """Automaicaly count method's call time"""
    in_key = method.__qualname__ + ":inputs"
    out_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(in_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(out_key, result)
        return result
    return wrapper


def replay(method: t.Callable):
    """Display the history of calls for a method"""
    r = redis.Redis()
    ins = r.lrange(method.__qualname__ + ":inputs", 0, -1)
    outs = r.lrange(method.__qualname__ + ":outputs", 0, -1)
    print(f"{method.__qualname__} was called {len(ins)}")
    for args, result in zip(ins, outs):
        print(f"{method.__qualname__}({args}) -> {result}")


class Cache:
    """Caching system based on redis"""
    def __init__(self) -> None:
        """Creates a connection to redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
