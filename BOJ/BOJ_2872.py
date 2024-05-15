import sys

# 책의 개수 N
N = int(sys.stdin.readline())
# 주어지는 책의 순서 books
books = [int(sys.stdin.readline()) for _ in range(N)]
# 사전순으로 가장 나중인 순서의 위치 idx
idx = books.index(N)

# 사전 순으로 쌓을 수 있는 횟수 answer
# N번째 뒤에 있는 수는 모두 이동이 필요하다
answer = N-1-idx
# 책 번호 N을 기준으로 answer을 설정 후 N-1부터 확인
N = N-1
for i in range(idx-1, -1, -1):
    # 이동이 필요하지 않은 경우
    if books[i] == N:
        N -= 1
    # 이동이 필요한 경우
    else:
        answer += 1

# 몇 번만에 책을 정렬할 수 있는지 출력
print(answer)