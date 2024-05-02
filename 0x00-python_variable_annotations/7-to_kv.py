#!/usr/bin/env python3
""" Module documentation """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Func to_kv doc"""
    return (k, v**2)
