import sys

# 자연수 N, 빈도를 구하는 한자리 숫자 D
N, D = map(str, sys.stdin.readline().split())
# 빈도수 answer
answer = 0

for i in range(1, int(N)+1):
    answer += str(i).count(D)
# 빈도수를 출력
print(answer)