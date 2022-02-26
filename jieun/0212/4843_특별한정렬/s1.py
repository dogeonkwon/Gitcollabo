# 4843_특별한정렬 풀이
# 2022-02-15

import sys
sys.stdin = open('input.txt', 'r')

#테스트 케이스 개수 가져와바
T = int(input())
#모든 테스트에 대해서
for t in range(1, T+1):
    #리스트의 길이를 가져와바!
    N = int(input())
    #리스트 갖고와!
    input_list = list(map(int, input().split()))
    #일단 sort를 해볼거야!
    for i in range(0, N):
        min_index = i
        for j in range(i+1, N):
            if input_list[min_index] > input_list[j]:
                min_index= j
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
    # 답을 찾을 list를 초기화하고 생서할게
    ans_list = []
    
    
    # k번째 큰 값, k번째 작은 값을 고를 함수를 만들자~
    def select_1(list, k):
        return list[N-k]
    def select_2(list, k):
        return list[k-1]


    #리스트를 반으로 나눠 그러니가 숫자가 10개니까 5번째 큰값, 5번째 작은 값까지 고를겅!
    for k in range(1, (int(N/2)) +1):
        ans_list.append(select_1(input_list, k))
        ans_list.append(select_2(input_list, k))
    
    # 출력하는 방법이 어렵군 ㅜ 테스트 케이스와 숫자 10개만 뽑으래 ㅡㅡ
    print('#{}'.format(t), end = ' ')
    for i in range(0, 10):
        if i == 9 :
            print(ans_list[i])
        else:
            print(ans_list[i], end = ' ')
