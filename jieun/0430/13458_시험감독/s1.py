import sys 
sys.stdin = open('input.txt','r')

N = int(input())
people = list(map(int, input().split()))
chong, bu = map(int, input().split())

manager_cnt = 0

# 전체 시험장 내 사람에서 총감독이 관할 할수 있는 사람 빼기
for n in range(N):
    if people[n] == 0:
        pass
    else: 
        if people[n] >= chong:
            people[n] -= chong
            manager_cnt +=1
        else:
            people[n] = 0
            manager_cnt +=1

# 부감독도 살펴보기
for n in range(N):
    if people[n] == 0:
        pass
    else:
        if people[n] % bu >0:
            people[n] = (people[n] // bu) +1
        elif people[n] % bu == 0:
            people[n] = people[n] // bu

for n in range(N):
    manager_cnt += people[n]

print(manager_cnt)
# manager_cnt와 부 감독 더해서 답내기
