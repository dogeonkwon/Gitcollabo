import sys
sys.stdin = open("input.txt", "r")

#len, sum 내장함수를 너무 쓰고 싶지만 쓰지 말라니까 이쁜 내가 참는다 휴,,
def my_len(arr):
    cnt = 0
    for i in arr:
        cnt +=1 
    return cnt
def my_sum(arr):
    sum = 0
    for i in arr:
        sum += i 
    return sum

#모든 테스트 케이스가 몇개인지 받아줘
T = int(input())
#그리고 1부터 12까지의 부분집합을 구할거니까 기본 arr을 만들어줘
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#모든 테스트 케이스를 살펴볼거야
for t in range(1, T+1):
    #부분집합 내의 원소가 몇개인지, 합은 몇인지 알아봐야겠지?
    N, K = map(int, input().split())
    
    cnt = 0
    #이건 교재에서 가져온 코드인데 의미는 조금더 살펴봐야될거 같아
    for i in range(1<<12):
        #부분집합을 만들 수 있는 빈 리스트를 만들어줘
        sub = []
        for j in range(12):
            #솔직히 여기 뭔소린지 모르겟음 멍멍
            if i&(1<<j):
                sub.append(arr[j])
        #부분집합을 전체 다 만들었다면 길이가 N인 합이 K인 부분집합의 숫자를 세줄거야
        if my_len(sub) ==N and my_sum(sub) ==K:
            cnt +=1
    print('#{} {}'.format(t, cnt))
