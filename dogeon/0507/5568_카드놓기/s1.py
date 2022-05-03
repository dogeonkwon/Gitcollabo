# 5568_카드놓기 풀이
# 2022-05-07


def pick(arr, picked, topick):
    global res

    # 인덱스번호 조합들의 개수가 k가 된다면 인덱스 번호에 맞는 cards 값들을 가져온 뒤 붙이고 res에 없다면 추가!
    if not topick:
        sub = ''
        for j in picked:
            sub += str(arr[j])
        if sub not in res:
            res.append(sub)
        return

    # 가질 수 있는 인덱스번호 조합들을 만들어준다.
    for i in range(n):
        if i not in picked:
            picked.append(i)
            pick(arr, picked, topick-1)
            picked.pop()

n = int(input())
k = int(input())
cards = [int(input()) for _ in range(n)]
res = list()    # 조합들을 담은 리스트
pick(cards, [], k)  # 조합을 찾을 함수
print(len(res))     # res의 길이가 정답!