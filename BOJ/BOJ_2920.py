import sys
# 주어지는 8개의 숫자를 담을 numbers
numbers = list(map(int, sys.stdin.readline().split()))
# 연주방법을 확인하기 위해 사용할 solution
solution = [0] * 7
# 인접한 두 음계의 차이를 solution에 담는다.
for i in range(7):
    solution[i] = numbers[i+1] - numbers[i]
# 모든 음계가 1차이가 난다면 ascending 출력
if solution.count(1) == 7:
    print('ascending')
# 모든 음계가 -1차이가 난다면 descending 출력
elif solution.count(-1) == 7:
    print('descending')
# 그외에 모든 경우 mixed 출력
else:
    print('mixed')