import math
def solution(fees, records):
    answer = []

    # 낮은 번호의 차량부터 정렬한다.
    car_num = set()
    for r in records:
        car_num.add(r[6:10])

    car_num = sorted(list(car_num))
    # ['0000', '0148', '5961']

    # 해당 번호의 입출차 기록을 담을 리스트
    times = []
    for c in car_num:
        tmp = []
        for r in records:
            # c 의 입,출차 기록을 찾는다.
            if c == r[6:10]:
                # c 차량의 입출차 기록을 tmp에 담는다.
                tmp.append(r[0:5])

        # tmp가 홀수라면 23:59분에 출차 했다고 기록        
        if len(tmp)%2:
            tmp.append('23:59')

        # 모든 기록을 times에 담는다.
        times.append(tmp)
        # [['06:00', '06:34', '18:59', '23:59'], ['07:59', '19:09'], ['05:34', '07:59', '22:59', '23:00']]
    
    # 주차 시간 계산 후 요금 정산
    for time in times:
        
        ans = 0
        # time의 홀수번째 인덱스는 IN, 짝수 인덱스는 OUT 이다. 
        for i in range (0,len(time),2):
            # 시 단위 계산 후 60곱해서 분으로 변환
            ans += abs(int(time[i][0:2])-int(time[i+1][0:2]))*60
            
            
            # 분 단위 계산
            # 입차 시간의 분 > 출차 시간의 분 (ex. 07:59 & 19:09) 이라면 위에서 계산한 값에서 빼야 하고
            if int(time[i][3:5]) > int(time[i+1][3:5]):
                ans -= int(time[i][3:5])-int(time[i+1][3:5])
            
            # 그렇지 않다면, 더한다.
            else:
                ans += abs(int(time[i][3:5])-int(time[i+1][3:5]))
        
        # 최종 요금 계산
        # 기본 시간 이하라면 기본 요금만 낸다.
        if ans < fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((ans - fees[0])/fees[2]) * fees[3])
    print(answer)
    return answer


solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])