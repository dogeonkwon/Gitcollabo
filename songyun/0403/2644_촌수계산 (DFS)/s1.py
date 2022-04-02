# 잘못한 점 : 만약 루트가 고조 할아버지인 경우, 할아버지와 손자간의 촌수가 4가 된다.

import sys
sys.stdin = open('input.txt')

def DFS(s):
    global cnt, grand

    v = s

    if not fm[v]:
        cnt = 0
        grand = v
        return

    while True:
        v = fm[v]
        cnt += 1
        # 만약 루트로 들어왔다면
        if not fm[v]:
            grand = v
            break


N = int(input())                        # 전체 사람 수
A, B = list(map(int, input().split()))  # 몇 촌인지 계산할 두 사람
M = int(input())                        # 부모 자식 관계 갯수

fm = [[] for _ in range(N+1)]                        # 트리
grand = 0


for i in range(M):
    p, c = list(map(int, input().split()))
    fm[c]=p

print(fm)
ans = 0
if fm[A] == fm[B]:
    ans = 2

elif fm[A] != fm[B]:
    cnt = 0
    grand = 0
    DFS(B)
    grand_1 = grand
    cnt_1 = cnt

    cnt = 0
    grand = 0
    DFS(A)
    grand_2 = grand
    cnt_2 = cnt

    if grand_1 == grand_2:
        ans = cnt_1 + cnt_2

    else:
        ans = -1


print(ans)

# DFS(A)
# print(cnt, grand)

# [[], [], [1], [1], [], [4], [4], [2], [2], [2]]


