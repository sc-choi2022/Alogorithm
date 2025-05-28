import sys

# 말의 개수 N
N = int(sys.stdin.readline())
# 말을 저장하는 배열 words
words = list(map(int, sys.stdin.readline().split()))
answer = -1

for i in range(N+1):
    cnt = words.count(i)

    if cnt == i:
        answer = max(answer, cnt)

# 참의 개수를 출력
# 내용이 모순인 경우 -1 출력
print(answer)