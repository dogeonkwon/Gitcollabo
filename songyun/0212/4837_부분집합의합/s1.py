import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N,K = map(int,input().split()) # N = 원소의 개수 , K = 부분의 집합의 합

    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    n = len(A)
    cnt = 0
    for i in range(1<<n): # 2^n개, 집합 A의 부분집합의 갯수만큼 반복하겠다
        part = list() # 부분집합을 넣을 list
        sum_1=0 # 부분의 집합의 합이 K가 되는지 확인할 변수

        # 집합의 갯수(12)만큼 j를 옮겨가면서 부분집합을 찾아 내겠다. 
        for j in range(n): # 이 반복문이 한번돌면 부분집합 케이스 한개가 나온다.   
            # j는 1, 10, 100 1000... 이렇게 12번 움직인다.
            if i&(1<<j): # ex) i가 3이면 0011,  j=1, 10 일 때만 if문 성립 (i,j를 이진수로 생각해야 함)
                part.append(A[j]) # A[0]원소를 part에 추가, 다음 반복 때 A[1] 추가 
                sum_1 += A[j] # 추가된 원소를 차례대로 sum_1에 더한다
        
        # 만들어진 부분집합의 갯수가 N 개이고, 그 합이 K 이면
        if len(part) == N and sum_1 == K:
            # 카운트를 한다.
            cnt+=1
    print("#{} {}" .format(tc, cnt))







