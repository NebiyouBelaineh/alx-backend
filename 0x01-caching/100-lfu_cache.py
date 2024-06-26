#!/usr/bin/env python3
"""LFU and LRU Caching"""

from base_caching import BaseCaching
from collections import OrderedDict, defaultdict


class LFUCache(BaseCaching):

    def __init__(self):
        super().__init__()
        self.freq = defaultdict(int)  # Frequency counter
        self.order = OrderedDict()  # Order for tie-breaking

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update existing key
            self.cache_data[key] = item
            self.freq[key] += 1
            self.order.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the LFU key(s)
                min_freq = min(self.freq.values())
                lfu_keys = [k for k, v in self.freq.items() if v == min_freq]
                # If there's a tie, use LRU among the LFU keys
                if len(lfu_keys) > 1:
                    lfu_key = None
                    for k in self.order:
                        if k in lfu_keys:
                            lfu_key = k
                            break
                else:
                    lfu_key = lfu_keys[0]
                # Discard the LFU/LRU key
                del self.cache_data[lfu_key]
                del self.freq[lfu_key]
                self.order.pop(lfu_key)
                print(f"DISCARD: {lfu_key}")

            # Add new key
            self.cache_data[key] = item
            self.freq[key] = 1
            self.order[key] = True

    def get(self, key):
        """Return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        self.order.move_to_end(key)
        return self.cache_data[key]
