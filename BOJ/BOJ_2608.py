import sys

def convert(N):
    result = 0
    lst = list(N)

    tmp = lst.pop(0)
    while lst:
        current = lst.pop(0)

        if tmp in ('IV', 'IX', 'XL', 'XC', 'CD', 'CM'):
            result += numbers[tmp]
            tmp = current
            continue

        if tmp != current:
            if numbers[tmp] > numbers[current]:
                result += numbers[tmp]
                tmp = current
            else:
                tmp += current
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

M1, M2 = convert(N1), convert(N2)