#!/usr/bin/env python3
""" LIFO Caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Caching """

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
                del self.cache_data[last]
                print("DISCARD: {}".format(last))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
