import math, sys

# 식단을 정할 일수 N
N = int(sys.stdin.readline())
# 음식의 리스트인 길이 N의 문자열 S
S = sys.stdin.readline().rstrip()

a = S.count('C')
b = len(S) - a

# 연속으로 치킨을 먹는 날의 최댓값의 최솟값 출력
print(math.ceil(a/(b+1)))

