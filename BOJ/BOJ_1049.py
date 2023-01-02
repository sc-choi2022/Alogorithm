import sys

# 끊어진 기타줄의 개수 N, 기타줄 브랜드 개수 M
N, M = map(int, sys.stdin.readline().split())

# 패키지의 가격을 담을 배열 package, 낱개의 가격을 담을 배열 each
package, each = [0] * M, [0] * M

for i in range(M):
    p, e = map(int, sys.stdin.readline().split())
    package[i], each[i] = p, e

# package와 each을 정렬
package.sort()
each.sort()

# 가능한 모든 돈의 경우의 수를 담은 배열 ans
ans = [package[0] * (N // 6 + 1), each[0] * N, package[0] * (N // 6) + each[0] * (N % 6)]
# ans의 최소값을 출력
print(min(ans))