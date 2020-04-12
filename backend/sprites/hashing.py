"""Hashing utilities"""

# Import standard library
import hashlib
from collections import deque
from typing import List, Tuple


def hasher(string: str) -> str:
    h = hashlib.sha224()
    h.update(string.encode("utf-8"))
    value = h.hexdigest()
    return "".join(filter(str.isdigit, value))


def get_seeds(h: str) -> Tuple[int, List[int]]:
    """Generate 10 seeds"""
    # The first 10 integers will make up the sprite
    sprite_seed = int(h[:9])
    color_seeds = [int("".join(n)) for n in window(h[::-1], 4)]
    return (sprite_seed, color_seeds)


def window(seq, n=4):
    it = iter(seq)
    win = deque((next(it, None) for _ in range(n)), maxlen=n)
    yield tuple(win)
    append = win.append
    for e in it:
        append(e)
        yield tuple(win)
