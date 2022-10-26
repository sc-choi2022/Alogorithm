import sys
# 주어지는 두수 A, B
A, B = sys.stdin.readline().strip().split()

# 출력할 곱셈 결과 ans
ans = 0
for a in A:
    a = int(a)
    for b in B:
        b = int(b)
        ans += a * b
# ans 출력
print(ans)