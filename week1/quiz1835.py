#1853
import sys
input=sys.stdin.readline
from collections import deque

N = int(input())
d=deque(i for i in range(N))
count=1
cardOrder=[0 for i in range(N)]#처음 카드 순서
while len(d):
    for i in range(count):
        d.append(d.popleft())
    cardOrder[d.popleft()]=count
    count+=1

print(" ".join(str(x) for x in cardOrder))