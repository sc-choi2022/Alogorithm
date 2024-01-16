import sys

# 단어의 개수 N
N = int(sys.stdin.readline())
# 단어를 저장하는 배열 words, 정렬
words = [sys.stdin.readline().rstrip() for _ in range(N)]
words.sort()

# 첫 번번째 단어 tmp와 그 길이 L
tmp= words[0]
L = len(tmp)
# 접두사 X의 부분집합의 최대 크기 answer
answer = 1

for i in range(1, N):
    # 부분집합에 포함되는 경우 answer 1 증가
    if tmp[:L] != words[i][:L]:
        answer += 1
    tmp = words[i]
    L = len(words[i])
# answer 출력
print(answer)