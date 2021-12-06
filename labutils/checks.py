import re


def is_float(num: str) -> bool:
    return bool(re.search(r"^[+-]?\d*\.?\d+([eE][+-]?\d+)?$", num))


def is_int(num: str) -> bool:
    return is_float(num) and float(num) % 1 == 0
