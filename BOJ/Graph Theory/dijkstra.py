import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start=int(input())
graph=[[]for i in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    node_1,node_2,cost=map(int,input().split())             #node1에서 node2로 가는 비용이 cost
    graph[node_1].append((node_2,cost))
    

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q(cost,i[0]))
                
dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])