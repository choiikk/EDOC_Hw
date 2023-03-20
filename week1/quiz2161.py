#2161
import sys
input=sys.stdin.readline

N = int(input())
que = [i+1 for i in range(N)]

while len(que)>1: #len(que)<=1이 되면 탈출
    #제일 위 카드를 바닥에 버린다
    print(que[0], end=" ")
    que.pop(0)
    #제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다
    que.append(que.pop(0))
    
    

print(que[0])


