#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier as argument and returns a function
    that multiplies a float by multiplier
    """
    def multi(floa: float) -> float:
        """multipli arg of the first def with the arg of the second def"""
        return (floa * multiplier)
    return(multi)
