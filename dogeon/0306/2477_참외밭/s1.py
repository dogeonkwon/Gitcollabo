# 2477_참외밭 풀이
# 2022-03-05


N = int(input())

lst = [list(map(int, input().split())) for _ in range(6)]

column = 0  # 제일 큰 가로 값을 담아줄 변수
row = 0     # 제일 큰 세로 값을 담아줄 변수
ran = [0, 1, 2, 3, 4, 5]        # 인덱스 번호를 비교하기 위한 리스트

for i in range(6):      # 육각형이라는 조건에 맞춰 가장 긴 세로, 가로변의 길이와 그 인덱스 번호를 저장해준다.
    if lst[i][0] == 1 or lst[i][0] == 2:
        if lst[i][1] > column:
            column = lst[i][1]
            column_index = i
    else:
        if lst[i][1] > row:
            row = lst[i][1]
            row_index = i

sub = [column_index, row_index]

if column_index == 0:   # 저장된 인덱스 번호의 양쪽 변의 값을 구해줘야 하는데 처음이거나 마지막일 경우를 가정해준다.
    sub += [5]
    sub += [1]
elif column_index == 5:
    sub += [0]
    sub += [4]
else:
    sub += [column_index + 1]
    sub += [column_index - 1]

if row_index == 0:
    sub += [5]
    sub += [1]
elif row_index == 5:
    sub += [0]
    sub += [4]
else:
    sub += [row_index + 1]
    sub += [row_index - 1]

result_index = [j for j in ran if j not in sub]     # 기존 인덱스번호에서 구해진 인덱스번호들을 빼준다.
min_area = 1
max_area = column * row     # 그렇게 구해진 변들을 이용해 빼야할 사각형의 넓이를 구해주고

for k in result_index:
    min_area *= lst[k][1]

result = (max_area - min_area) * N      # 전체 사각형의 넓이에서 빼준다.

print(result)