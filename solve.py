from collections import deque
import sys
input=sys.stdin.readline
dy,dx=[0,0,1,-1],[1,-1,0,0] #동 서 남 북
weight,eat,can_eat,sol=2,0,0,0
def bfs(y,x,eat, weight,time,can_eat):
    dq=deque()
    chk=[[False]*n for _ in range(n)]
    chk_lst=[]
    mapp[y][x]=0
    dq.append([y,x,eat,weight,time])
    while dq:
        y,x,eat,weight,time=dq.popleft()
        chk[y][x]=True
        time+=1
        for i in range(4):
            ny,nx=y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<n and chk[ny][nx]==False:
                if mapp[ny][nx]==0 or mapp[ny][nx]==weight:
                    dq.append([ny,nx,eat,weight,time])
                elif 0<mapp[ny][nx]<weight:
                    chk_lst.append([ny,nx,eat,weight,time])
    if len(chk_lst)==0:
        return y,x,eat,weight,time,0
    chk_lst.sort(key=lambda p:(p[4],p[0],p[1]))
    y,x,eat,weight,time=chk_lst[0]
    mapp[y][x]=9
    eat+=1
    if eat==weight:
        eat=0
        weight+=1
    return y,x,eat,weight,time,len(chk_lst)
n=int(input())
mapp=[list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if mapp[i][j] == 9:
            y,x=i,j
while True:
    y,x,eat,weight,time,can_eat=bfs(y,x,eat,weight,0,can_eat)
    if can_eat==0:
        break
    sol+=time
print(sol)