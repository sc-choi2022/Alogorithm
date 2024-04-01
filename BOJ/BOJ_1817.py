import sys

# 책의 개수 N, 박스에 넣을 수 있는 최대 무게 M
N, M = map(int, sys.stdin.readline().split())
# 책이 존재하는 경우
if N:
    books = list(map(int, sys.stdin.readline().split()))
    # 필요한 박스의 개수 answer
    answer = 0

    # 현재 박스에 넣는 책의 무게 mass
    mass = 0

    for book in books:
        if mass + book <= M:
            mass += book
        else:
            answer += 1
            mass = book
    # 필요한 박스의 개수 출력
    print(answer+1 if mass else answer)
else:
    # 0 출력
    print(0)