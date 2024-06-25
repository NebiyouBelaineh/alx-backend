#!/usr/bin/env python3
"""FIFO Caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching"""

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = next(iter(self.cache_data))
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
