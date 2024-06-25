#!/usr/bin/env python3
"""MRU Caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU Caching"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if (
                len(self.cache_data) >= BaseCaching.MAX_ITEMS
                    and key not in self.cache_data):
                last = self.order.pop(0)
                del self.cache_data[last]
                print("DISCARD: {}".format(last))
            self.cache_data[key] = item
            self.order.insert(0, key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.insert(0, key)
        return self.cache_data.get(key)
