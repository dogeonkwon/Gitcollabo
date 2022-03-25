# 1861_정사각형-방 풀이
# 2022-03-16

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    loc = [None] * (N * N + 2)     # 인덱스 = 방 번호, 값 = 방번호가 있는 좌표 값
    arr = [0] * N                  # 방 N*N

    # loc 만들기
    for i in range(N):
        arr[i] = list(map(int, input().split()))
        for j in range(N):
            loc[arr[i][j]] = [i, j]

    room_num = 0       # 방 번호를 임시 저장할 변수
    cnt = 1            # 카운팅 변수
    result = [0, 0]    # 0: 방번호, 1: 횟수
    n = 1              # 1 ~ N*N 까지 탐색
    while n < N*N+1:
        # 만일, 카운팅을 시작한다면 시작 방번호 저장
        if cnt == 1:
            room_num = int(arr[loc[n][0]][loc[n][1]])

        si = loc[n][0]
        sj = loc[n][1]
        stop = 0         # 방을 찾았는지 확인할 변수

        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            # 상하좌우에 다음 방번호가 있다면
            if 0 <= si + di < N and 0 <= sj + dj < N and [si+di, sj+dj] == loc[n+1]:
                cnt += 1    # 횟수 +1
                n += 1      # 다음 방으로 이동
                stop = 1    # 방을 찾았다 !
                break

        # 상하좌우에 방이 없다면
        if stop == 0:
            # 연속된 방이 기존에 연속된 방의 개수보다 많다면, 방번호와 개수를 바꿔줌
            if result[1] < cnt:
                result[0] = int(room_num)
                result[1] = int(cnt)
            cnt = 1
            n += 1

    print('#{}'.format(tc), *result)