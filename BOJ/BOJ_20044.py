import sys

# 팀의 수 N
N = int(sys.stdin.readline())

# 학생의 코딩역량을 저장하는 배열 numbers
numbers = sorted(list(map(int, sys.stdin.readline().split())))
# Sm 값 answer
answer = sum(numbers)
for i in range(N):
    answer = min(answer, numbers[i]+numbers[-(i+1)])
# Sm 값을 출력
print(answer)