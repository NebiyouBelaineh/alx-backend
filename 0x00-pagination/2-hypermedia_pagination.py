#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple, Dict, Union


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple containing the start and end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


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

    def get_hyper(self, page: int = 1, page_size: int = 10
                  ) -> Dict[str, Union[int, List[List]]]:
        """Returns a dictionary containing key-value pairs as a
        hypermedia pagination
        - page_size: the length of the returned dataset page
        - page: the current page number
        - data: the dataset page (equivalent to return from previous task)
        - next_page: number of the next page, None if no next page
        - prev_page: number of the previous page, None if no previous page
        - total_pages: the total number of pages in the dataset as an integer
        """
        response = {
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if (self.get_page(page + 1, page_size)
                                      != []) else None,
            "prev_page": page - 1 if page > 1 and (
                self.get_page(page - 1, page_size) != []) else None,
            "total_pages": math.ceil(len(self.dataset()) / page_size)
        }
        return response
