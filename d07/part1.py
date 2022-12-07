from contextvars import copy_context
import os
from shlex import split as split_cmd_line
from typing import DefaultDict, List
from util import get_data

def join_path(*paths) -> str:
    return os.path.join(*paths).replace("\\", "/")

lines: List[str] = get_data(("\n"))

def tuple_list():
    return ([], [])

print(tuple_list() is tuple_list())

dirs = DefaultDict(tuple_list)
dirs["/"] = tuple_list()
pwd = ["/"]


def get_cwd():
    return "/" + '/'.join(pwd[1:])

d = "/"

# lines = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k""".split("\n")

for line in lines:
    if not line: continue
    line = split_cmd_line(line)
    if line[0] == "$":#
        line.pop(0)
        if line.pop(0) == "cd":
            if line[0] == "..":
                pwd.pop()
            elif line[0] == "/":
                pwd = ["/"]
            else:
                pwd.append(line[0])
            print("cd ", line[0], pwd)
        
        else:  # ls x?
            d = get_cwd()
            if len(line) >= 1:
                d = join_path(d, line[0])

    elif line[0] == "dir":
        dirs[join_path(d, line[1])] = tuple_list()
        dirs[d][0].append(join_path(d, line[1]))
    
    else:
        dirs[d][1].append((line[1], int(line[0])))
        
# print(dirs)
def size(directory: str, start_size = 0) -> int:
    d = dirs[directory]
    for sub_dir in d[0]:
        start_size += size(sub_dir)
    
    for file in d[1]:
        start_size += file[1]
        
    return start_size

count = 0
for dir in dirs:
    s = size(dir)
    if s <= 100000:
        count += s
print(count)