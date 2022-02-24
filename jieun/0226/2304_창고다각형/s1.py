import sys
sys.stdin = open('input.txt', 'r')

# 빌딩의 개수
N = int(input())
# 건물의 끝 위치, 가장 높은 빌딩의 크기, 빌딩의 위치와 크기를 담을 비어있는 리스트 생성
end_location = 0
max_building = 1
building_lst =[]
#빌딩의 개수 만큼 가져옴
for n in range(N):
    #빌딩의 인덱스와, 빌딩의 크기
    i, H = map(int,input().split())
    building_lst.append([i,H])
    # 빌딩의 끝 위치와 가장 높은 빌딩의 크기, 가장 높은 빌딩의 위치를 구하기
    if end_location <  i:
        end_location = i
    if max_building <H:
        max_building = H
        max_location = i

#빌딩의 인덱스와 크기를 받아서 그 인덱스에 그 빌딩을 넣어서 순차적으로 정렬
building_list = [0]*(end_location+1)
for i, h in building_lst:
    building_list[i] = h

#면적을 구할 변수
area = 0
# 건물의 크기를 담을 변수 생성
building = 0
# 처음부터 가장 높은 빌딩이 있는 위치까지 순차적으로 빌딩의 크기를 더해감
for location in range(max_location+1):
    if building_list[location] > building:
            building = building_list[location]
    area += building
# 마지막부터 가장 높은 빌딩이 있는 위치까지 순차적으로 빌딩의 크기를 더해감
building = 0
for location in range(end_location, max_location, -1):
    if building_list[location] > building:
        building = building_list[location]
    area += building
#지금까지 왼쪽과 오른쪽 면적을 더해준 area 변수 출력
print(area)
