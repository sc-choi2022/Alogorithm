import sys

# 책의 개수 N, 한 번에 들 수 있는 책의 개수 M
N, M = map(int, sys.stdin.readline().split())
# 책의 위치 books
books = list(map(int, sys.stdin.readline().split()))
books.sort()

# 음수, 양수의 위치를 저장하는 배열 neg, pos
neg, pos = [], []
for book in books:
    if book < 0:
        neg.append(book)
    else:
        pos.append(book)

# 움직이는 걸음 수 answer, 돌아오지 않는 마지막 위치 distance
answer, distance = 0, 0

for j in range(0, len(neg), M):
    answer += -neg[j]*2
    distance = max(distance, -neg[j])

for k in range(len(pos)-1, -1, -M):
    answer += pos[k]*2
    distance = max(distance, pos[k])

# 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 출력
print(answer-distance)