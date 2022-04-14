# 5014_스타트링크 풀이
# 2022-04-16


def dfs_U(s, cnt):

    if s+U <= F and not floor[s+U]:
        floor[s+U] = cnt
        if floor[G]:
            return
        dfs_U(s+U, cnt+1)
    if s-D > 0 and not floor[s-D]:
        floor[s-D] = cnt
        if floor[G]:
            return
        dfs_U(s-D, cnt+1)


def dfs_D(s, cnt):

    if s-D > 0 and not floor[s-D]:
        floor[s-D] = cnt
        if floor[G]:
            return
        dfs_D(s-D, cnt+1)
    if s+U <= F and not floor[s+U]:
        floor[s+U] = cnt
        if floor[G]:
            return
        dfs_D(s+U, cnt+1)


F, S, G, U, D = map(int, input().split())   # F : 최대 층 / S : 현재 위치 / G : 목적지 / U : 올라갈 수 있는 층수 / D : 내려갈 수 있는 층수
floor = [0] * (F+1)
floor[S] = 1
if S < G and U:
    i = (G-S) // U
    j = (i*U) + S
    floor[j] = i
    dfs_U(j, i+1)
elif S > G and D:
    n = (S-G) // D
    m = S - (n*D)
    floor[m] = n
    dfs_D(m, n+1)

if floor[G]:
    print(floor[G])
else:
    print('use the stairs')

