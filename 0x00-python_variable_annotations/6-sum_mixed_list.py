#!/usr/bin/env python3
"""module task 6"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns their sum of a list as a float"""
    return float(sum(mxd_lst))
