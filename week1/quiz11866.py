import sys
input = sys.stdin.readline

N, K = map(int, input().split())
que = list(i+1 for i in range(N))
resultSequence="<"

#반복: que가 빌때까지 반복. len(que)>0일동안 반복
while len(que)>1:
    #K-1회 앞으로 당겨서 K번째 사람이 front에 오게 하기
    for i in range(K-1):
        que.append(que.pop(0))
        
   
    #front에 있는 사람 제거
    resultSequence+=str(que[0])+", "
    que.pop(0)

resultSequence+=str(que[0])+">"
print(resultSequence)

