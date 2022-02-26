import sys
sys.stdin = open("input.txt")
# 이진탐색을 할 수 있는 함수를 만들거야 얍~
def binarySearch(page, key):
    #첫 페이지를 넣어줘
    page_start = 1
    # 마지막 페이지도 설정할거야
    page_end = page
    # 몇번 탐색을 했는지 count를 해줄거야
    cnt =0
    #페이지 스타트가 페이지 엔드보다 작을 동안
    while page_start <= page_end:
        #중간 페이지를 탐색하는 것이므로 중간 페이지도 변수를 넣어줄게
        middle = int((page_start + page_end)/2)
        #만약 내가 찾고자하는 값이 중간값과 똑같다면
        if key == middle:
            #cnt에 따로 카운트 하지 않고 바로 출력해줘
            return cnt
        #만약 내가 찾고자하는 값이 중간값보다 작다면
        elif key < middle:
            #처음부터 중간값까지 중에서 다시 살펴볼거야
            page_end = middle
            #탐색한번 한거니까 count 세줘!
            cnt +=1 
        #만약 내가 찾고자하는 값이 중간값보다 크다면
        else:
            #중간값부터 끝페이지 중에서 다시 살펴볼거야
            page_start = middle
            #탐색한번 한거니까 count 세줘!
            cnt +=1

#모든 테스트 케이스 수를 넣어줘
T = int(input())
# 모든 테스트 케이스 중에서 
for t in range(1, T+1):
    # 책의 페이지 끝과, A,B가 찾아야하는 페이지 수를 받아줘
    page, A, B = map(int, input().split())
    # A,B가 찾아야하는 페이지를 찾을 때까지 카운트 한 수를 받아줘
    countA = binarySearch(page, A)
    countB = binarySearch(page, B)
    # 만약 A가 더 많이 카운트했다면 B가 이긴거야!
    if countA > countB:
        result = "B"
    #만약 B가 더 많이 카운트했다면 A가 이긴거야!
    elif countA < countB:
        result = "A"
    #둘다 아니라면 비긴거야!
    else:
        result = 0
    print('#{} {}'.format(t, result))