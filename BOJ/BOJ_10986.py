import sys

# 주어지는 수의 개수 N, 나누어 떨어지는 기준 수 M
N, M = map(int, sys.stdin.readline().split())

# N개의 숫자를 담은 리스트 lst
lst = list(map(int, sys.stdin.readline().split()))

# 구간의 개수 ans
ans = 0

# M으로 나누었을 떄 나머지를 담을 리스트 remainder
remainder = [0 for i in range(M)]
# 누적합을 담을 변수 presum
presum = 0

remainder[0] = 1

for i in range(N):
    # 누적합을 생성하고
    presum += lst[i]
    # 그 누적합의 나머지를 remainder리스트에 나머지값을 인덱스로 추가해준다.
    remainder[presum % M] += 1

# 나머지를 담은 리스트 remainder에서 조합으로 2개를 뽑는 방법으로 값을 ans에 누적해준다.
for i in remainder:
    ans += i*(i-1)//2

# ans 출력
print(ans)