#!/usr/bin/env python3
"""Task module with tools for request caching and tracking.
"""
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()
"""The module-level Redis instance.
"""

def data_cacher(method: Callable[[str], str]) -> Callable[[str], str]:
    """Caches the output of fetched data.
    """
    @wraps(method)
    def invoker(url: str) -> str:
        """The wrapper function for caching the output.
        """
        # Increment the request count
        redis_store.incr(f'count:{url}')
        
        # Check if the result is already cached
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        
        # Fetch the result, cache it, and return it
        result = method(url)
        redis_store.setex(f'result:{url}', 10, result)
        return result

    return invoker

@data_cacher
def get_page(url: str) -> str:
    """Returns the content of a URL after caching the request's response,
    and tracking the request.
    """
    return requests.get(url).text
