import sys

def solve1(inp):
    ans = 0
    for i in inp.split():
        l = len(i)
        a = i[:l//2]
        b = i[l//2:]
        a = set(a)
        b = set(b)
        c = a.intersection(b)
        c = c.pop()
        if c == c.lower():
            ans += ord(c)-ord('a')+1
        else:
            ans += ord(c)-ord('A')+27
    return ans

def solve2(inp):
    inp = inp.split()
    ans = 0
    for i in range(0, len(inp), 3):
        a = set(inp[i])
        b = set(inp[i+1])
        c = set(inp[i+2])
        c = c.intersection(b)
        c = c.intersection(a)
        c = c.pop()
        if c == c.lower():
            ans += ord(c)-ord('a')+1
        else:
            ans += ord(c)-ord('A')+27
    return ans

f = open("day3.in", "r")
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