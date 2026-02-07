from math import ceil
import sys

# 식단을 정할 일수 N
N = int(sys.stdin.readline())
# 음식의 리스트인 길이 N의 문자열 S
S = sys.stdin.readline().rstrip()

# C의 개수 a
a = S.count('C')

# 연속으로 치킨을 먹는 날의 최댓값의 최솟값 출력
print(ceil(a/(N-a+1)))