#10773
import sys
input=sys.stdin.readline

K = int(input())
stack=list()

for i in range(K):
    num = int(input())
    if(num):#0이 아닐 때
        stack.append(num)
    else:#0일 때
        stack.pop()

print(sum(stack))