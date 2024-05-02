#!/usr/bin/env python3
""" Module documentation """
from typing import Mapping, Any, Union, TypeVar

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """Func safely_get_value doc"""
    if key in dct:
        return dct[key]
    else:
        return default
