import sys
sys.stdin = open('input.txt','r')

# dfs하기
def dfs(start):
    stack = []
    stack.append(start)
    
    # 연결되어있는 노드에 바로 추가
    for node in graph[start]:
        if visited[node] == 0:
            visited[node] =1
            dfs(node)
    return visited

N = int(input())
# 간선의 개수
line = int(input())
visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]
# 시작한 컴퓨터와 도착한 컴퓨터 작성
for l in range(line):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    
cnt = 0
ans = dfs(1)
#지금까지 visited라는 리스트에 1이 추가되어있으면 바로 cnt 추가
for i in range(len(ans)):
    if ans[i] == 1:
        cnt +=1
print(cnt)