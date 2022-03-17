import sys
sys.stdin = open('input.txt','r')


def dfs(start):
    stack = []

    stack.append(start)

    for node in graph[start]:
        if visited[node] == 0:
            visited[node] =1
            dfs(node)
    return visited

N = int(input())
line = int(input())
visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for l in range(line):
    start, end = map(int, input().split())
    graph[start].append(end)

cnt = 0
ans = dfs(1)
for i in range(len(ans)):
    if ans[i] == 1:
        cnt +=1
print(cnt)