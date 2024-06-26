#!/usr/bin/env python3
"""LRUCache class"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last = self.order.pop(0)
                if last != key:  # decides to replace instead of remove
                    del self.cache_data[last]
                    print("DISCARD: {}".format(last))
            self.cache_data[key] = item
            self.order.append(key)
        else:
            return

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key)
