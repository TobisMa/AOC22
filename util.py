import datetime
from typing import Tuple, Optional, List


def get_data(delimiter: Tuple[str, ...] = ("\n",), __current: Optional[List] = None, day = None, skip_empty = True, type_=None, file=None):
    day = f"d{get_day():0>2}" if day is None else f"d{day:0>2}"
    if file is None:
        file = day + "/data.txt"
        
    if not delimiter:
        if __current is not None:
            return __current

        with open(file, "r") as f:
            return f.read()

    elif __current is None:
        with open(file, "r") as f:
            text = f.read()

        __current = text.split(delimiter[0])

    else:
        if type_ is None or len(delimiter) >= 2:
            type_ = lambda x: x
        __current = [list(map(type_, [y for y in x.split(delimiter[0]) if y])) for x in __current if x]

    return get_data(delimiter[1:], __current=__current, day=int(day[-2:]), skip_empty=True, type_=type_, file=file)
    
    

def get_day() -> int:
    return datetime.datetime.now().day