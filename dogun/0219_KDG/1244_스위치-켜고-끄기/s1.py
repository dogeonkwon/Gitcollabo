# 1244_스위치-켜고-끄기 풀이
# 2022-02-19

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())    # 스위치 개수

on_off = list(map(int, input().split()))    # 스위치 상태

T = int(input())    # 학생수

for tc in range(T):

    gender_number = list(map(int, input().split()))     # 성별과 숫자 담을 리스트

    if gender_number[0] == 1:       # 남학생일 경우
        v = gender_number[1] - 1    # 인덱스 값
        w = gender_number[1]        # 배수만큼 증가시켜줄 증가값

        while v < N:
            on_off[v] = on_off[v] * (-1) + 1    # 스위치 개수보다 인덱스 값이 작으면 스위치 상태변환
            v += w

    else:                           # 여학생일 경우
        n = gender_number[1] - 1    # 인덱스 값
        m = 1                       # 증가(감소)시켜줄 값
        on_off[n] = on_off[n] * (-1) + 1            # 기본적으로 기준점을 우선 변경
        while (n-m) >= 0 and (n+m) <= (N-1):
            if on_off[n-m] == on_off[n+m]:          # 기준점에서 -m, +m하였을 때 상태가 같다면 변경
                on_off[n-m] = on_off[n-m] * (-1) + 1
                on_off[n+m] = on_off[n+m] * (-1) + 1
                m += 1
            else:
                break

for i in range(0, N, 20):       # 20번째마다 다음 차례는 줄을 바꿔서 출력하도록 함
    print(*on_off[i:i+20])