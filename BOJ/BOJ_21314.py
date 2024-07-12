import sys

# 주어지는 민겸 수 number
numbers = sys.stdin.readline().rstrip()
# 십진수로 변환되었을 때 가질 수 있는 값 중 가장 큰 값 answerMax, 가장 작은 값 answerMin
answerMax, answerMin = '', ''
# M의 개수 cnt
cnt = 0

for number in numbers:
    if number == 'M':
        cnt += 1
    else:
        if cnt == 0:
            answerMax += '5'
            answerMin += '5'
        else:
            answerMax += '5' + '0' * cnt
            answerMin += '1' + '0' * (cnt-1) + '5'
        cnt = 0

if cnt:
    answerMax += '1'*cnt
    answerMin += '1' + '0'*(cnt-1)

# 가장 큰 값과 가장 작은 값을 두 줄로 나누어 출력
print(answerMax)
print(answerMin)