# BOJ_1244_스위치켜고끄기 풀이
# 2022-02-17
# 데이터 받아오기
import sys
sys.stdin = open('input.txt', 'r')

# 스위치를 켜고 끄는 함수를 보여줄게 얍!
def on_off(num):
    if current[num] ==0:
        current[num] =1
    else:
        current[num] = 0
    return

#스위치의 개수
switch_count = int(input())
#스위치가 꺼져있는지 켜져있는지 여부
current = [0] + list(map(int, input().split()))

# 학생수
students = int(input())
# 성별과 받은 수
for _ in range(students):
    sex, num = map(int, input().split())
    # 성별이 남자라면
    if sex == 1:
        # 배수를 구해볼거야!
        n = 1
        # 길이 안에 있을 때까지 num*1, num*2 등등의 배수의 스위치 조절하기
        while n * num < len(current):
            on_off(num *n)
            n+=1
    # 성별이 여자라면
    else:
        #
        on_off(num)
        for k in range(switch_count//2):
            if num + k > switch_count or num -k <1:
                break
            if current[num+k] == current[num -k]:
                on_off(num+k)
                on_off(num-k)
            else:
                break

for i in range(1, switch_count+1):
    print(current[i], end = " ")
    if i % 20 ==0:
        print()