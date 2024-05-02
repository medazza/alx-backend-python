#!/usr/bin/env python3
""" Module documentation """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Func safe_first_element doc"""
    if lst:
        return lst[0]
    else:
        return None
