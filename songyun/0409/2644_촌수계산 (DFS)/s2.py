import sys
sys.stdin = open('input.txt')

def DFS(s):
    visited[s] = True

    for i in fm[s]:
        if not visited[i]:
            level[i] = level[s] + 1
            DFS(i)


N = int(input())                        # 전체 사람 수
A, B = list(map(int, input().split()))  # 몇 촌인지 계산할 두 사람
M = int(input())                        # 부모 자식 관계 갯수

fm = [[] for _ in range(N+1)]           # 부모 자식 관계가 담긴 list
visited = [False] * (N+1)
level = [0] * (N+1)                     # A를 기준으로 각 노드가 몇 촌 관계인지 담을 list

# 양방향 으로 가족관계를 담는다.
for i in range(M):
    p, c = list(map(int, input().split()))

    fm[p].append(c)
    fm[c].append(p)

# fm = [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2, 10], [2], [2], [7]]

DFS(A)

# 만약 B번 인덱스에 1 이상의 수가 있다면 촌수가 존재 한다는 의미
if level[B] > 0:
    print(level[B])

# 그렇지 않다면 촌수 확인 불가
else:
    print(-1)

