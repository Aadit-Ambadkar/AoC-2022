import sys

def solve1(inp):
    ans = 0
    for i in (inp.split("\n")):
        c1, c2 = i.split()
        c1=ord(c1)-ord("A")
        c2=ord(c2)-ord("X")
        ans+=c2+1
        if (c1+1)%3==c2:
            ans+=6
        elif c1==c2:
            ans+=3
    return ans

def solve2(inp):
    ans = 0
    for i in (inp.split("\n")):
        c1, c2 = i.split()
        c1=ord(c1)-ord("A")
        c2=ord(c2)-ord("X")
        if c2==0:
            ans += ((c1+2)%3)+1
        elif c2==1:
            ans += 3 + c1 + 1
        else:
            ans += 6 + ((c1+1)%3)+1
    return ans

f = open("day2.in", "r")
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