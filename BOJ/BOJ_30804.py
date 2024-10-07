from collections import defaultdict
import sys

# 과일의 개수 N
N = int(sys.stdin.readline())
# 과일 번호를 저장하는 배열 fruits
fruits = list(map(int, sys.stdin.readline().split()))
# 과일의 개수를 저장하는 배열 number
number = [0] * 10

# 과일 종류의 개수를 세는 탕후루의 범위 left, right
left, right = 0, 0
# 1번 과일의 개수를 저장
number[fruits[0]] = 1
# 과일의 개수가 가장 많은 탕후루의 과일 개수 answer
# 최소 개수 1로 값 초기화
answer = 1

while right < N-1:
    right += 1
    number[fruits[right]] += 1

    # 과일이 두 종류 이상인 경우
    if number.count(0) < 8:
        while True:
            number[fruits[left]] -= 1
            left += 1
            if number.count(0) >= 8:
                break
    # answer 값 갱신
    answer = max(answer, right-left+1)

# answer 출력
print(answer)