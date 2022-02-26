# 2116_주사위-쌓기 풀이
# 2022-02-19

import sys

sys.stdin = open('input.txt', 'r')


# 리스트 내에서 가장 큰 수 반환
def max_num(lst):
    m = lst[0]
    for l in lst:
        if m < l:
            m = l
    return m


# 옆면 중 가장 큰 수 반환
def max_plus(lst, ii):
    ll = list(lst)
    if ii % 2:
        ll.pop(ii)
        ll.pop(ii - 1)
    else:
        ll.pop(ii + 1)
        ll.pop(ii)
    return max_num(ll)


N = int(input())  # 주사위 개수
dice = list()  # 주사위도면 받아오기

for n in range(N):
    v = list(map(int, input().split()))
    # 마주보는 면끼리 묶기
    # 0,1 / 2, 3 / 4, 5
    v[1], v[2], v[3], v[4], v[5] = v[5], v[1], v[3], v[2], v[4]
    dice.append(v)

# 1. 합을 저장할 리스트
# sums = list()
max_s = 0

# 첫번째 주사위를 기준으로 구함
for i in range(6):
    s = max_plus(dice[0], i)  # 합 초기화(밑면과 윗면을 제외하고 가장 큰 수)
    value = dice[0][i]  # 윗면의 값(초기값)
    idx = 0  # 윗면 아랫면을 찾아줄 인덱스

    # 두번째 주사위부터 쌓기
    for j in range(1, N):
        # 밑면의 값에 해당하는 수의 인덱스
        # 밑면의 값을 윗면의 값으로 전환
        # 합 + 밑면과 윗면을 제외하고 가장 큰 수
        idx = dice[j].index(value)
        value = dice[j][idx - 1] if idx % 2 else dice[j][idx + 1]
        s += max_plus(dice[j], idx)
    if s > max_s:
        max_s = s
    # 1. 각 경우에서 구한 최대합을 sums 리스트에 저장
    # sums.append(s)

# 1. 한 옆면의 숫자의 합이 가장 큰 경우 출력
# max_s = max_num(sums)
print(max_s)
