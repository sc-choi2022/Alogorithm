import sys

def convert(N):
    result = 0
    lst = list(N)
    # 변환하는 로마 숫자를 저장하는 변수 tmp
    tmp = lst.pop(0)
    while lst:
        current = lst.pop(0)
        # tmp가 보통의 규칙이 아닌 로마 숫자인 경우
        if tmp in ('IV', 'IX', 'XL', 'XC', 'CD', 'CM'):
            result += numbers[tmp]
            tmp = current
            continue
        # 반복되는 로마 숫자가 아닌 경우
        if tmp != current:
            if numbers[tmp] > numbers[current]:
                result += numbers[tmp]
                tmp = current
            else:
                tmp += current
        # 반복되는 로마 숫자인 경우
        else:
            result += numbers[tmp]
            tmp = current
    result += numbers[tmp]

    return result

numbers = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
           'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

# 로마 숫자로 표현된 수 N1, N2
N1 = sys.stdin.readline().rstrip()
N2 = sys.stdin.readline().rstrip()
# N1과 N2를 어한 아라비아 숫자 num, num을 출력
num = convert(N1)+convert(N2)
print(num)

# 로마 숫자를 저장하는 문자열 answer
answer = ''
while num:
    if num >= 1000:
        answer += 'M'
        num -= 1000
    elif num >= 900:
        answer += 'CM'
        num -= 900
    elif num >= 500:
        answer += 'D'
        num -= 500
    elif num >= 400:
        answer += 'CD'
        num -= 400
    elif num >= 100:
        answer += 'C'
        num -= 100
    elif num >= 90:
        answer += 'XC'
        num -= 90
    elif num >= 50:
        answer += 'L'
        num -= 50
    elif num >= 40:
        answer += 'XL'
        num -= 40
    elif num >= 10:
        answer += 'X'
        num -= 10
    elif num >= 9:
        answer += 'IX'
        num -= 9
    elif num >= 5:
        answer += 'V'
        num -= 5
    elif num >= 4:
        answer += 'IV'
        num -= 4
    elif num >= 1:
        answer += 'I'
        num -= 1

# answer을 출력
print(answer)