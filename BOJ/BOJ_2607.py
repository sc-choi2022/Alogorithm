import sys

# 단어의 개수 N
N = int(sys.stdin.readline())
# 첫번째 단어 first
first = list(sys.stdin.readline().rstrip())
# 첫 번째 단어와 비슷한 단어의 개수 answer
answer = 0
for _ in range(N-1):
    # 첫번째 단어 first의 비교를 위한 배열 compare
    compare = first[::]
    # 주어지는 단어 word
    word = sys.stdin.readline().rstrip()
    # 빼야하는 문자의 개수 cnt
    cnt = 0
    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1
    # 하나의 문자를 더하거나, 빼거나, 바꾸면 비슷한 단어가 되는 경우 answer 1 증가
    if cnt < 2 and len(compare) > 2:
        answer += 1
# answer 출력
print(answer)