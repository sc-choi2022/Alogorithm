import sys

# 지워지고 남은 숫자들 numbers
numbers = sys.stdin.readline().rstrip()
# 각 위치의 숫자의 최소 수를 확인하는 수 cnt
cnt = 0

while numbers:
    cnt += 1
    num = str(cnt)
    # number와 numbers의 길이비교가 가능한 경우
    while num and numbers:
        if num[0] == numbers[0]:
            numbers = numbers[1:]
        num = num[1:]
# 가능한 N 중에 최솟값을 출력
print(cnt)