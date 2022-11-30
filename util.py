import datetime
from typing import Tuple, Optional, List


def get_data(delimiter: Tuple[str, ...] = ("\n",), __current: Optional[List] = None, day = None, skip_empty = True, type_=None):
    day = f"d{get_day():0>2}" if day is None else f"d{day:0>2}"

    if not delimiter:
        if __current is not None:
            return __current

        with open(day + "/data.txt", "r") as f:
            return f.read()

    elif __current is None:
        with open(day + "/data.txt", "r") as f:
            text = f.read()

        __current = text.split(delimiter[0])

    else:
        __current = [x.split(delimiter[0]) for x in __current if skip_empty and x]

    if skip_empty:
        __current = [x for x in __current if x]
    if type_ is not None:
        __current = list(map(type_, __current))
    return get_data(delimiter[1:], __current=__current, day=int(day[-2:]), skip_empty=True, type_=type_)
    
    

def get_day() -> int:
    return datetime.datetime.now().day