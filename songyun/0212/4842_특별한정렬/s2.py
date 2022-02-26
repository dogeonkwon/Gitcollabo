# 4843_특별한정렬
# 22-02-15

import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 정수의 갯수
    a = list(map(int, input().split())) # 새롭게 정렬할 리스트
    j =0
    
    # while이 한 번 돌면 두개의 원소가 정렬돼. 32번째 줄을 보면 왜 while을 이렇게 했는지 이해가 될거야 
    while j < 10: # 0 -> 2 -> 4 -> 6 -> 8  
        
        # max,min을 각각 왼쪽으로 옮길거야 
        for i in range(j,N):
            if a[j] <= a[i]: # 홀수번째에 max를 넣고,
                a[j], a[i]= a[i], a[j]
            elif a[j+1] >= a[i]: # 짝수번째에 min을 넣고, 
                a[j+1],a[i] = a[i],a[j+1]

        j+=2 # 반복 한 번으로 두 개의 원소를 정렬 했으므로 2 올려준다. 
    
    # swea의 출력예시와 맞추기 위해 이렇게 했어
    print("#{}".format(tc), end=" ") # 몇 번째 케이스 인지 출력
    for i in range(9):
        print("{}".format(a[i]), end=" ") # 숫자 사이사이를 띄어쓰기 해줘

    # 위 반복문으로 마지막 원소를 출력하면 뒤에 공백이 생겨 Fail이 돼. 그래서 마지막 원소는 따로 출력했어
    print(a[9])


        

