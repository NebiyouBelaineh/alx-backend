#!/usr/bin/env python3
"""Module containing inde_range function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple containing the start and end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
