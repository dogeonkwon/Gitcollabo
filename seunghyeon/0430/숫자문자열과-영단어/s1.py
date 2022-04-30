# 2022-04-28

def solution(s):
    numbers = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
    }

    # python에서 replace는 특정문자열을 원하는 문자열로 바꿔준다.
    # 변경횟수를 지정해주지 않으면 default로 모두 변경 !
    for num in numbers:
        s = s.replace(num, numbers[num])

    answer = int(s)
    return answer