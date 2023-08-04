#!/usr/bin/env python3
"""Complex types - mixed list  """

from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """ Return sum of list of floats """
    return float(sum(mxd_lst))
