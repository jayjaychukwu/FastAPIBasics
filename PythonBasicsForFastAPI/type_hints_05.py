from typing import Optional, Tuple


def greeting(name: Optional[str] = None) -> str:
    return f"Hello, {name if name else 'Anonymous'}"


IntStringFloatTuple = Tuple[int, str, float]

t: IntStringFloatTuple = (1, "hello", 3.14)
