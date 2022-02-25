# 2309_일곱-난쟁이 풀이
# 2022-02-26


def long(sub):
    cnt = 0
    for _ in sub:
        cnt += 1
    return cnt


def func(i, N, s, t):    # i - 시작 원소인덱스 // N - 원소의 개수 // s - 이전까지 고려된 원소의 합 // t - 목표값
    global lst
    if s == t:                  # 목표값을 찾으면
        sub = list()
        for j in range(N):              # 비트가 1인지 아닌지 검사하기 위해 N번 만큼 반복문 가동
            if bit[j]:                  # 비트가 1이라면 같은 자리의 a리스트의 j번째 번호를 출력
                sub.append(arr[j])
        lst.append(sub)

    elif i == N:                  # 더이상 고려할 원소가 없으면
        return
    elif s > t:                  # 고려한 원소의 합 s가 이미 목표를 초과한 경우
        return
    else:                           # 비트가 처음에는 0이었으므로 1로 바꿔주고 검사하고
        bit[i] = 1
        func(i+1, N, s + arr[i], t)
        bit[i] = 0                  # 다시 0으로 바꿔서 검사해본다.
        func(i+1, N, s, t)


N = 9                                  # 원소의 개수만큼

arr = list()
for _ in range(9):
    arr += map(int, input().split())

bit = [0]*N                             # 이진수 동작할 bit 리스트
lst = list()                            # 조건을 만족하는 부분 집합의 리스트들을 모아둘 곳
t = 100                                  # t(목표값)가 되는 경우가 있는가?
func(0, N, 0, t)                           # 함수는 내가 어떤 조건을 달기 나름 / 조건을 잘 달수록 연산횟수가 줄어듬


for i in lst:
    if long(i) == 7:
        i.sort()
        for j in i:
            print(j)

# 99
# 100
# 1
# 2
# 3
# 4
# 5
# 6
# 79