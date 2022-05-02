def solution(s):
    dict_1 = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    dict_2 = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }

    ans = ''
    tmp = ''

    for i in s:
        tmp += i

        if tmp in dict_1:
            ans += str(dict_1[tmp])
            tmp = ''

        elif tmp in dict_2:
            ans += i
            tmp = ''

    return int(ans)

# 입출력 예
# "one4seveneight"	1478
# "23four5six7"	234567
# "2three45sixseven"	234567
# "123"	123