import sys

# 수열의 크기 N
N = int(sys.stdin.readline())
# 수열 A
A = sys.stdin.readline().rstrip()

add = 0
tmp = ''

for a in A:
    if a.isdigit():
        tmp += a
    else:
        add += int(tmp)
        tmp = ''
add += int(tmp)

print(add-sum(range(1, int(N))))