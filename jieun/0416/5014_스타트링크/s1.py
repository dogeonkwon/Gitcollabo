import sys
sys.stdin = open('input.txt','r')


def bfs(start):
    global ans
    queue = []
    queue.append((start, 0))
    visited[start] = 1
    ans = F

    while queue:
        s, cnt = queue.pop(0)
        if s == G:
            ans = min(ans, cnt)
            break
        if s+ U <= F and visited[s+U] == 0:
            queue.append((s+U, cnt+1))
            visited[s+U] =1
        if s-D >= 1 and visited[s-D] == 0:
            queue.append((s-D,cnt+1))
            visited[s-D] = 1

T = int(input())
for t in range(1, T+1):
    F, S, G, U, D = map(int, input().split())
    visited= [0] * (F+1)
    bfs(S)


    if ans == F:
        print('use the stairs')
    else:
        print(ans)
