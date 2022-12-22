import sys

# 다솜이의 방번호 N
N = sys.stdin.readline().strip()

# 방번호의 각 번호의 개수를 세는 딕셔너리 numbers
numbers = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}

for n in N:
    # 6과 9인 경우
    if n == '6' or n == '9':
        numbers['6'] += 1
    else:
        numbers[n] += 1

# numbers['6']의 수를 조건에 맞게 계산
numbers['6'] = numbers['6'] // 2 + 1 if numbers['6'] % 2 else numbers['6'] // 2

# 필요한 세트의 개수를 출력
print(max(numbers.values()))