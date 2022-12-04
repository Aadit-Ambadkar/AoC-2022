import sys

def solve1(inp):
    ans = 0
    for i in inp.split():
        pass
    return ans

def solve2(inp):
    ans = 0
    for i in inp.split():
        pass
    return ans

f = open("day<REP>.in", "r")
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