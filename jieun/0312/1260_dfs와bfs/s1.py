from collections import deque
import sys
sys.stdin = open('input.txt','r')


#dfs
def dfs(v):
    visited[v] = 1
    print(v, end = " ")
    for node in graph[v]:
        if visited[node] ==0:
            dfs(node)


#bfs
def bfs(v):
    visited[v] = 1
    q = deque()
    q.append(v)
    while q:
        x = q.popleft()
        print(x, end=" ")
        for node in graph[x]:
            if visited[node] == 0:
                q.append(node)
                visited[node] = 1

N, M, V = map(int, input().split())
graph= [[] for _ in range(N+1)]
visited = [0] * (N+1)
for m in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, N+1):
    graph[i].sort()

dfs(V)
visited=[0] * (N+1)
print()
bfs(V)