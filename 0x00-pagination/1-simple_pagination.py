#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """"Returns a list that is paginated using index_range function"""
        assert (isinstance(page, int) and isinstance(page_size, int))
        assert ((page != 0) and (page_size != 0))
        assert ((page > 0) and (page_size > 0))

        range = index_range(page, page_size)
        start, end = range[0], range[1]

        dataset = self.dataset()
        return dataset[start: end]
