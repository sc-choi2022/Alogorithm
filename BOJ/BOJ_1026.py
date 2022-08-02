import sys
# 배열의 길이 N
N = int(sys.stdin.readline())
# 정수 배열 A, B
# 재배열이 가능한 A는 sorted을 활용하여 정렬한다.
A = sorted(list(map(int, sys.stdin.readline().split())))
B = list(map(int, sys.stdin.readline().split()))

# 출력할 최소값 S
ans = 0
# S가 최소가 되기 위해서 B는 가장 큰 값을 곱해주고 B에서 제거한다.
for a in A:
    ans += a * B.pop(B.index(max(B)))
# ans을 출력
print(ans)