from asyncio import proactor_events
from typing import List, Literal
from util import get_data


data = get_data("\n")
# data = """addx 15
# addx -11
# addx 6
# addx -3
# addx 5
# addx -1
# addx -8
# addx 13
# addx 4
# noop
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx -35
# addx 1
# addx 24
# addx -19
# addx 1
# addx 16
# addx -11
# noop
# noop
# addx 21
# addx -15
# noop
# noop
# addx -3
# addx 9
# addx 1
# addx -3
# addx 8
# addx 1
# addx 5
# noop
# noop
# noop
# noop
# noop
# addx -36
# noop
# addx 1
# addx 7
# noop
# noop
# noop
# addx 2
# addx 6
# noop
# noop
# noop
# noop
# noop
# addx 1
# noop
# noop
# addx 7
# addx 1
# noop
# addx -13
# addx 13
# addx 7
# noop
# addx 1
# addx -33
# noop
# noop
# noop
# addx 2
# noop
# noop
# noop
# addx 8
# noop
# addx -1
# addx 2
# addx 1
# noop
# addx 17
# addx -9
# addx 1
# addx 1
# addx -3
# addx 11
# noop
# noop
# addx 1
# noop
# addx 1
# noop
# noop
# addx -13
# addx -19
# addx 1
# addx 3
# addx 26
# addx -30
# addx 12
# addx -1
# addx 3
# addx 1
# noop
# noop
# noop
# addx -9
# addx 18
# addx 1
# addx 2
# noop
# noop
# addx 9
# noop
# noop
# noop
# addx -1
# addx 2
# addx -37
# addx 1
# addx 3
# noop
# addx 15
# addx -21
# addx 22
# addx -6
# addx 1
# noop
# addx 2
# addx 1
# noop
# addx -10
# noop
# noop
# addx 20
# addx 1
# addx 2
# addx 2
# addx -6
# addx -11
# noop
# noop
# noop""".split("\n")

class CRT:
    
    def __init__(self) -> None:
        self.signal_strengths = []
        self.__x: int = 1
        self.__cycle: int = 0
        self.area: List[List[str]] = [[' ' for _ in range(40)] for _ in range(6)]
    
    def cycle(self) -> None:
        self.__cycle += 1
        self.draw()
    
    def addx(self, x: int) -> None:
        self.cycle()
        self.cycle()
        self.__x += x
    
    @property
    def sum(self) -> int:
        return sum(self.signal_strengths)
    
    def draw(self) -> None:
        row: int = (self.__cycle - 1) // 40
        column: int = (self.__cycle - 1) % 40
        pixel: Literal['#', ' '] = "#" if column in range(self.__x - 1, self.__x + 2) else " "
        self.area[row][column] = pixel
        
        
crt = CRT()
    
for line in data:
    if line == "noop":
        crt.cycle()
    
    elif line.startswith("addx"):
        crt.addx(int(line.split()[-1]))

for row in crt.area:
    print(' '.join(row))