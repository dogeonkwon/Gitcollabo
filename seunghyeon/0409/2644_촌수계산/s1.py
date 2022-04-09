# BOJ_2644_촌수계산
# 2022-04-06


def parent(v, visited):
    global visit

    if not visit[v]:         # 방문한 노드가 아니면
        visit[v] = True      # 방문표시
        visited.append(v)    # 조상노드를 추가
        if par[v] == 0:      # root까지 왔으면 return
            return
        parent(par[v], visited)  # 추가적인 조상노드 찾기
    else:
        visited.append(v)   # 이미 방문한 노드면 해당노드까지 넣고 return
        return


n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
par = [0] * (n+1)
visit = [False] * (n+1)
cnt = -1
first = []
second = []

# 자식노드를 인덱스로 부모노드 저장
for _ in range(m):
    p, c = map(int, input().split())
    par[c] = p

parent(p1, first)    # p1의 조상노드 찾기
parent(p2, second)   # p2의 조상노드 찾기

# 만일 겹치는 조상이 있다면, 이들은 친척관계
if second[-1] in first:
    for f in first:
        cnt += 1
        if second[-1] == f:
            break
    cnt += len(second)-1
else:
    cnt = -1

print(cnt)