import sys

def solve1(inp):
    return sorted([sum(map(int,i.split("\n")))for i in inp.split("\n\n")])[-1:][0]

def solve2(inp):
    return sum(sorted([sum(map(int,i.split("\n")))for i in inp.split("\n\n")])[-3:])


f = open("day1.in", "r")
inp = f.read()
if len(sys.argv) < 2:
    print(solve1(inp))
elif sys.argv[1]=="-1":
    print(solve1(inp))
elif sys.argv[1]=="-2":
    print(solve2(inp))
else:
    print("what you doing?")

f.close()