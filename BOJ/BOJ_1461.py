import sys

# 책의 개수 N와 한번에 들 수 있는 책의 개수 M
N, M = map(int, sys.stdin.readline().split())
# 책의 위치를 저장하는 books
books = sorted(list(map(int, sys.stdin.readline().split())))
idx = 0
for i in range(N):
    if books[i] > 0:
        idx = i
        break
B1, B2 = books[:idx], books[idx:]
B2.reverse()
L1, L2 = len(B1), len(B2)
answer = 0

for j in range(0, L1, M):
    answer -= 2*B1[j]

for k in range(0, L2, M):
    answer += 2*B2[k]

if B1 and B2:
    answer -= max(-B1[0], B2[0])
elif B1 and not B2:
    answer -= -B1[0]
elif not B1 and B2:
    answer -= B2[0]

print(answer)