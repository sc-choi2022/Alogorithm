import sys

while True:
    line = sys.stdin.readline().rstrip('\n')

    if not line:
        break
# 소문자, 대문자, 숫자, 공백의 개수 lower, upper, number, blank
    lower, upper, number, blank = 0, 0, 0, 0

    for l in line:
        if l == ' ':
            blank += 1
        elif 65 <= ord(l) <= 90:
            upper += 1
        elif 97 <= ord(l) <= 122:
            lower += 1
        else:
            number += 1
    print(lower, upper, number, blank)