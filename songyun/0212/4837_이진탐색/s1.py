# 4839_이진탐색
# 22-02-15

import sys
sys.stdin=open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    P, A, B= map(int, input().split()) # P=전체 페이지, A,B=A와 B가 찾아야 하는 페이지

    # A와 B 각각의 경우를 따로 계산했기 때문에 변수 또한 각각 지정
    # 시작 페이지
    IA = 1 
    IB = 1 

    # 마지막 페이지
    PA = P 
    PB = P 

    # 중간 페이지
    CA = int((IA+PA)/2)
    CB = int((IB+PB)/2)
    cntA = 0
    cntB = 0

    # 절반으로 나눈 값이 목표 페이지와 같지 않다면 반복
    while CA != A :
        
        # 중간 페이지가 목표 페이지 보다 크다면
        if CA > A :
            # 마지막 페이지를 중간 페이지로 변경
            PA = CA
            CA = int((IA+PA)/2)
            cntA+=1
        
        # 중간 페이지가 목표 페이지 보다 작다면
        else:
            # 시작 페이지를 중간 페이지로 변경
            IA = CA
            CA = int((IA+PA)/2)
            cntA+=1
    
    # A와 동일
    while CB != B :
        
        if CB > B :
            PB = CB
            cntB+=1
            CB = int((IB+PB)/2)
        else:
            IB = CB
            cntB+=1
            CB = int((IB+PB)/2)

    # 카운트가 적은 사람을 출력
    if cntA < cntB:
        print("#{} A".format(tc))
    elif cntB < cntA:
        print("#{} B".format(tc))
    else:
        print("#{} 0".format(tc))


# 창완이형 방식
# import sys
# sys.stdin = open('input.txt', 'r')
#
# T = int(input())
#
# def binary_search(target, n):
#     start = 1
#     end = n
#     cnt = 0
#     while start <= end:
#         mid = (start + end) // 2
#         cnt += 1
#         # 같을경우 값을 찾은 경우이므로 횟수를 리턴한다
#         if mid == target:
#             return cnt
#         # 찾는 값이 높을 경우 start 에 중앙값을 넣는다
#         elif mid < target:
#             start = mid
#         # 찾는 값이 낮을 경우 end 값에 중앙값을 넣는다
#         else:
#             end = mid
#     return None
#
#
# for t in range(1, T+1):
#     N, A, B = map(int, input().split())
#     # 이진함수 호출
#     a_cnt = binary_search(A, N)
#     b_cnt = binary_search(B, N)
#     # 결과값 비교
#     if a_cnt < b_cnt:
#         ans = 'A'
#     elif a_cnt > b_cnt:
#         ans = 'B'
#     else:
#         ans = 0
#
#     print('#{} {}'.format(t, ans))