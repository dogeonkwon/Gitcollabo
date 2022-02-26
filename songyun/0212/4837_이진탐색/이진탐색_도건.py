# import sys
# sys.stdin = open('sample_input.txt', 'r')


# 1번 풀이.

# T = int(input())
#
# for tc in range(1, T+1):
#
#     P, A, B = map(int, input().split())
#
#     cnt = 1
#     result = int(P/2)
#
#     cnt_2 = 1
#     result_2 = int(P/2)
#
#
#     while result != A:
#
#         if A > result:
#             result = int((result + P) / 2)
#             cnt += 1
#         else:
#             result = int((result + 1) / 2)
#             cnt += 1
#
#     while result_2 != B:
#
#         if A > result_2:
#             result_2 = int((result_2 + P) / 2)
#             cnt_2 += 1
#         else:
#             result_2 = int((result_2 + 1) / 2)
#             cnt_2 += 1
#
#     if cnt > cnt_2:
#         end = 'A'
#     elif cnt < cnt_2:
#         end = 'B'
#     else:
#         end = 0
#
#     print('#{} {}'.format(tc, end))



#----------------------------------------------------------------------------------------


# 2번 풀이.


# import sys
# sys.stdin = open('sample_input.txt', 'r')
#
#
# # 우선 이진 탐색을 하기 위한 함수를 만들어준다.(전체 값이 담긴 리스트, 찾고자 하는 값)
# def binary_search(p, num):
#
#     # 리스트 p를 탐색하기 위해 시작값은 0으로 잡는다.
#     # 마지막 값을 설정하기 위해 p에서 1을 빼준다.
#     # 얼만큼 수행하였는지 횟수를 비교하기 위해 cnt를 1로 잡아준다.(처음 수행하여서 바로 맞추더라도 수행횟수가 1이 되므로)
#     start = 0
#     end = p - 1
#     cnt = 1
#
#     # start(시작값)이 end(마지막)값보다 커지는 순간 절반이상, 모든 탐색을 다 했다는 의미이므로 start <= end로 설정해준다.
#     # middle(중간값)은 시작값과 (마지막 값 - 시작값)을 2로 나눈 것이 된다.
#     # ex) 시작값이 100, 마지막 값이 500이라면 중간값은 300이 된다.(다른 수를 대입해도 마찬가지)
#     while start <= end:
#         middle = int((end - start)/2)
#
#         # num(찾고자 하는 값)이 p의 중간값과 같다면 바로 cnt를 리턴해준다.
#         if num == middle:
#             return cnt
#
#         # num이 p의 중간값보다 크다면 리스트 방향에서 오른쪽으로 중간값 찾기를 진행해야 하므로 start에 middle + 1을 해주며 횟수를 1 더해준다.
#         elif num > middle:
#             start = middle
#             cnt += 1
#
#         # num이 p의 중간값보다 작다면 리스트 방향에서 왼쪽으로 중간값 찾기를 진행해야 하므로 end에 middle - 1을 해주며 횟수를 1 더해준다.
#         else:
#             end = middle
#             cnt += 1
#
#     return cnt



# T = int(input())
#
# for tc in range(1, T+1):
#     P, A, B = map(int, input().split())
#
#     # P의 갯수만큼 정렬된 숫자들을 받는 lst를 만들어준다.
#     lst = []
#     for i in range(1, P+1):
#         lst.append(i)
#
#     # result_A는 lst에서 A의 값을 찾기위해 수행한 횟수이다.
#     result_A = binary_search(lst, A)
#
#     # result_B는 lst에서 B의 값을 찾기위해 수행한 횟수이다.
#     result_B = binary_search(lst, B)
#
#     # result_A와 result_B의 결과를 비교하여 승자를 가린다.
#     if result_A > result_B:
#         winner = 'B'
#     elif result_A < result_B:
#         winner = 'A'
#     else:
#         winner = 0
#
#     print('#{} {}'.format(tc, winner))

# T = int(input())
#
# for tc in range(1, T + 1):
#     page, A, B = map(int, input().split())
#
#     countA = binary_search(page, A)
#     countB = binary_search(page, B)
#
#     if countA > countB:
#         result = 'B'
#     elif countA < countB:
#         result = 'A'
#     else:
#         result = 0
#     print("#{} {}".format(tc, result))


#------------------------------------------------------------------------------------------


# 3번 풀이

import sys
sys.stdin = open("sample_input.txt")

# 이진 탐색을 하는 함수를 만들어준다.(책의 마지막 쪽 번호, 찾고자 하는 번호)
def binary_search(page, target):

    # left = 첫 번째 번호
    # right = 오른쪽 값 = 마지막 페이지 번호
    # cnt = 초기 횟수 값
    left = 1
    right = page
    count = 0

    # 왼쪽 값이 오른쪽 값보다 커진다면 while문 종료
    while left <= right:

        # 중간값을 찾기 위함
        middle = int((left + right) / 2)

        # 중간값과 찾고자 하는 값과 같으면 그대로 cnt를 리턴
        if middle == target:
            return count

        # 찾고자 하는 값보다 중간값이 작다면 left에 중간값을 넣어줘서 오른쪽으로 탐색할 수 있도록 한다.
        elif middle < target:
            left = middle
            count += 1

        # 찾고자 하는 값보다 중간값이 크다면 right에 중간값을 넣어줘서 왼쪽으로 탐색할 수 있도록 한다.
        elif middle > target:
            right = middle
            count += 1


T = int(input())
for tc in range(1, T + 1):
    page, A, B = map(int, input().split())

    result_A = binary_search(page, A)
    result_B = binary_search(page, B)

    # 선언한 함수를 실행시켜 A와 B의 횟수를 비교해준다.
    if result_A > result_B:
        winner = 'B'
    elif result_A < result_B:
        winner = 'A'
    else:
        winner = 0

    print("#{} {}".format(tc, winner))



