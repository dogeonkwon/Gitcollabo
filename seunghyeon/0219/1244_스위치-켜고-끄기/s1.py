# 1244_스위치-켜고-끄기 풀이
# 2022-02-19
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())                            # 스위치 개수
switch = list(map(int, input().split()))    # 스위치 상태
students = int(input())                     # 학생수

for _ in range(students):
    gender, num = map(int, input().split())  # 성별, 스위치 번호
    num = num - 1                            # 스위치 번호 -1

    # 남자일때,
    if gender == 1:
        # 배수 다 바꿔줌
        for n in range(num, N, num+1):
            switch[n] = int(not(switch[n]))
        continue

    # 여자일때,
    if gender == 2:
        # 자기 스위치 번호에 해당하는 값 스위칭
        switch[num] = int(not(switch[num]))
        a = 1

        # num-a와 num+a가 인덱스범위 내에 있을 때
        while num-a >= 0 and num+a < N:
            # 양 옆의 값이 같으면 바꿔준다
            if switch[num-a] == switch[num+a]:
                switch[num-a] = int(not(switch[num-a]))
                switch[num+a] = int(not(switch[num+a]))
                a += 1
            else:
                break

a = 0
while a < N:
    if (a+1) % 20 == 0:
        print(switch[a])
        a += 1
        continue
    print(switch[a], end=' ')
    a += 1
