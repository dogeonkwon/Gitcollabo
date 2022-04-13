import sys
sys.stdin = open('input.txt','r')


# dfs를 해서 안으로 계속 들어감
def dfs(s_tart):
    for node in graph[s_tart]:
        if node != s_tart and visited[node]== 0:
            visited[node] = visited[s_tart] +1
            dfs(node)


N = int(input())
# 시작 노드부터 끝 노드까지
start, end = map(int, input().split())
# 연결된 간선 
line = int(input())
# 가족 트리와 방문햇는지 distance역할도 같이 해줄 visited
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
# 가족트리에 양방향으로 넣어줌
for i in range(line):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

dfs(start)

# 만약 도달하지 않았다먄 -1 출력, 도달했다면 촌수 계산
if visited[end] == 0:
    print(-1)
else:
    print(visited[end])