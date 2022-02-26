import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 정수의 갯수
    a = list(map(int, input().split())) # 새롭게 정렬할 리스트
    j =0

    # while이 한 번 돌면 두개의 원소가 정렬돼. 32번째 줄을 보면 왜 while을 이렇게 했는지 이해가 될거야 
    while j < 10: # 0 -> 2 -> 4 -> 6 -> 8  
        # max1=a[0+j] # 최댓값 기준 
        # min1=a[0+j] # 최솟값 기준

        # min,max 판별
        for i in range(j,N):
            if a[j] <= a[i]:
                a[j], a[i]= a[i], a[j]
            elif a[j+1] >= a[i]:
                a[j+1],a[i] = a[i],a[j+1]
            
        # max를 먼저 앞으로 보내고, min을 그 뒤로 보낼거야
        for k in range(N):
            # a[k]가 max 라면
            if max1 == a[k]: 
                a[j],a[k]=a[k],a[j] # a[k]를 미정렬된 맨앞의 숫자와 자리 바꿔
            # a[k]가 min 이라면
            elif min1 == a[k]: 
                a[j+1],a[k]=a[k],a[j+1] # a[k]를 max 뒤에 있는 숫자와 자리 바꿔 
        
        # [0][1]에 max,min을 넣었으므로 그 다음인 [2][3] 탐색을 위해 j에 2 더해
        j+=2

    # swea의 출력예시와 맞추기 위해 이렇게 했어
    # ex) #1 10 1 9 2 8 3 7 4 6 5
    print("#{}".format(tc), end=" ") # 몇 번째 케이스 인지 출력
    for i in range(9):
        print("{}".format(a[i]), end=" ") # 숫자 사이사이를 띄어쓰기 해줘

    # 위 반복문으로 마지막 원소를 출력하면 뒤에 공백이 생겨 Fail이 돼. 그래서 마지막 원소는 따로 출력했어
    print(a[9])

    # join을 써보자..

        

