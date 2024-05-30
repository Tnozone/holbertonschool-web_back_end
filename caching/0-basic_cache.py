#!/usr/bin/env python3
""" Basic Cache module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """bsic dictionary"""

    def put(self, key, item):
        """ Puts item in cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Gets item from cache """
        if key is None:
            return None
        return self.cache_data.get(key, None)
