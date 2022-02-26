# 부분집합의-합
# 2022-02-12

import sys

# input.txt 불러오기
# 테스트 케이스
sys.stdin = open('sample_input.txt', 'r')
T = int(input())

for tc in range(1, T+1):

    # N: 부분집합 원소의 개수, K: 부분집합의 각 원소들의 합
    # A: 1에서 12까지의 숫자를 원소로 가진 집합
    # parts: N개의 원소를 가지고, 원소들의 합이 K인 A의 부분집합들
    # result: 결과
    N, K = map(int, input().split())
    A = [n for n in range(1, 13)]
    parts = list()
    result = 0

    # 부분집합 구하기
    for i in range(1 << 12):
        cnt = 0                # N개의 원소 카운팅
        part = list()          # 임시의 부분집합들 저장

        for j in range(12):

            # 부분집합 생성 part
            # 원소의 개수 구하기
            if i & (1 << j):
                cnt += 1
                part.append(A[j])

        # 부분집합의 원소의 개수가 N이면, parts에 부분집합을 추가
        # 부분집합 part와 원소의 개수 N 초기화
        if cnt == N:
            parts.append(part)
            part = []
            cnt = 0

    # 부분집합 각 원소들의 합 구하기
    for p in parts:
        val = 0

        # 각 원소들의 합을 구한 후
        for i in p:
            val += i

        # 원소들의 합이 K인 경우, result +1  및 합 초기화화
        if val == K:
            result += 1
            val = 0

    print('#{} {}'.format(tc, result))
