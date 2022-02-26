# 색칠하기
# 2022-02-12

import sys

# input.txt 불러오기
# 테스트 케이스
sys.stdin = open('sample_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):

    # N: 색칠할 영역의 개수
    # space: 2차원 배열
    # cnt: 보라색 개수
    N = int(input())
    space = list()
    cnt = 0

    # 하지마세요 !!!!!! 얕은 복사 주의 !!!!!!
    # space = [[0]*10] *10

    # 2차원 배열 만들기
    for m in range(10):
        space.append([0] * 10)

    for n in range(N):
        # 페인트 위치와 색상을 받아온다.
        paint = list(map(int, input().split()))

        # 빨강(1)일때, 겹치는 부분을 구하기 위해 3으로 바꾼다.
        if paint[4] == 1:
            paint[4] = 3

        # 색칠하기
        for a in range(paint[0], paint[2]+1):
            for b in range(paint[1], paint[3]+1):
                # 값이 0일때는 색깔에 해당하는 수를 입히고,
                # 0이 아닌 경우, 곱한다.
                if space[a][b] != 0:
                    space[a][b] *= paint[4]

                else:
                    space[a][b] = paint[4]

    # 빨강(3), 파랑(2)이 둘 다 칠해진 경우, 2*3이 무조건 있기 때문에
    # 6으로 나눈 나머지가 0이다.
    for i in range(10):
        for j in range(10):
            if (space[i][j] % 6) == 0 and space[i][j] != 0:
                cnt += 1

    print('#{} {}'.format(tc, cnt))
