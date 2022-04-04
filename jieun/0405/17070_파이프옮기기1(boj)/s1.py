import sys
sys.stdin = open('input.txt','r')


def pipe(i, j, direction):
    global ans
    # 종료조건
    if i == N-1 and j== N-1:
        ans +=1
    
    # 들어가기
    # 1. 지금 파이프 방향이 가로다
    if direction == 'row':
        # 1) 가로
        if j+1<N and arr[i][j+1] == 0:
            pipe(i, j+1, 'row')
        # 2) 대각선
        if i+1 < N and j+1 <N:
            if arr[i][j+1] == 0 and arr[i+1][j+1] == 0 and arr[i+1][j] == 0:
                pipe(i+1, j+1, 'diag')
    
    # 2. 지금 파이프 방향이 세로다
    elif direction == 'column':
        # 1) 세로
        if i+1<N and arr[i+1][j] == 0:
            pipe(i+1, j, 'column')
        # 2) 대각선
        if i+1 < N and j+1 <N:
            if arr[i][j+1] == 0 and arr[i+1][j+1] == 0 and arr[i+1][j] == 0:
                pipe(i+1, j+1, 'diag')
    # 2. 지금 파이프 방향이 대각선이다
    elif direction == 'diag':
        # 1) 가로
        if j+1<N and arr[i][j+1] == 0:
            pipe(i, j+1, 'row')
        # 2) 세로
        if i+1<N and arr[i+1][j] == 0:
            pipe(i+1, j, 'column')
        # 3) 대각선
        if i+1 < N and j+1 <N:
            if arr[i][j+1] == 0 and arr[i+1][j+1] == 0 and arr[i+1][j] == 0:
                pipe(i+1, j+1, 'diag')



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
pipe(0,1, 'row')
print(ans)