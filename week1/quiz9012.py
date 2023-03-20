import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    str=input().strip()
    stack = list()
    for i in str:
        stack.append(i)
        if(len(stack)>1 and stack[-2]=='(' and stack[-1]==')' ):
            stack.pop()
            stack.pop()
    if(len(stack)):
        print("NO")
    else:
        print("YES")