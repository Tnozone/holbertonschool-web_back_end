#!/usr/bin/python3

""" Basic Cache
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic dictionary"""

    def put(self, key, item):
        """Puts item in cache"""
        if item is not None and key is not None:
            self.cache_data[key] = {item}

    def get(self, key):
        """Retreave item from cache"""
        return self.cache_data.get(key, None)
