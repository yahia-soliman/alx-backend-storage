#!/usr/bin/env python3
"""Web caching with Redis"""
import redis
import requests

r = redis.Redis()


def get_page(url: str) -> str:
    """Get a web page, cache it for 10 seconds"""
    cached = r.get(url)
    if isinstance(cached, bytes):
        html = cached.decode()
    else:
        res = requests.get(url)
        html = res.text
        r.set(url, html, ex=10)

    r.incr(f"count:{url}")
    r.expire(f"count:{url}", 10)
    return html
