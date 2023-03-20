#1021
import sys
input=sys.stdin.readline
from collections import deque

N,M = map(int, input().split())#입력1
deleteNums=list(map(int, input().split()))#입력2
d = deque(i+1 for i in range(N))

sum=0 #결과출력

for deleteNum in deleteNums: 
    while(d[0]!=deleteNum):
        if(d.index(deleteNum)>len(d)/2):
            #3번연산(오른쪽으로 한칸 이동)    
            d.appendleft(d.pop())
        else:
            #2번연산(왼쪽으로 한칸 이동)
            d.append(d.popleft())
        sum+=1
    #d[0]==deleteNum일때 뽑아낸다
    d.popleft()

print(sum)
    
    






