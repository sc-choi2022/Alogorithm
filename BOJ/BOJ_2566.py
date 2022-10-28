import sys
# 9×9 격자판에 쓰여진 81개의 자연수 또는 0을 담은 배열 numbers
numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
# 출력할 최댓값, 위치한 행 번호와 열 번호 max_value, row, col
max_value, row, col = 0, 0, 0

# 각 numbers에 idx, number에서 최대값을 확인
for idx, number in enumerate(numbers):
    # max_value보다 큰값이 number에 있는 경우
    if max(number) > max_value:
        # max_value, row, col 값을 재저장
        max_value = max(number)
        row = idx
        col = number.index(max_value)
# max_value 출력
print(max_value)
# 행 번호와 열 번호 출력
print(row + 1, col + 1)