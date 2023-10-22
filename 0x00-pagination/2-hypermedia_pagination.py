#!/usr/bin/env python3
'''
    Simple pagination.
'''
import csv
import math
from typing import List


def index_range(page, page_size):
    '''
        Returns the range of indexes for a given page.
    '''
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"
