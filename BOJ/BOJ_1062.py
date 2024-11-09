import sys

def dfs(idx, cnt):
    global answer

    # K의 문자를 가르친 경우
    if cnt == K:
        reading = 0
        for word in words:
            for w in word:
                if not visit[ord(w)-97]:
                    break
            else:
                reading += 1
        answer = max(answer, reading)
        return

    for i in range(idx, 26):
        if not visit[i]:
            visit[i] = 1
            dfs(i+1, cnt+1)
            visit[i] = 0

# 단어의 개수 N, 가르칠 수 있는 글자의 개수 K
N, K = map(int, sys.stdin.readline().split())
# 단어를 이루는 알파벳을 저장하는 배열 words
words = [set(list(sys.stdin.readline().rstrip())) for _ in range(N)]

# 남극언어를 읽을 수 없는 경우
if K < 5:
    print(0)
# 남극언어를 읽을 수 있는 경우
else:
    # 배운 글자를 확인하는 배열 visit
    # 단어의 기본 글자를 1로 초기화
    visit = [0] * 26
    visit[0], visit[2], visit[8], visit[13], visit[19] = 1, 1, 1, 1, 1

    # 읽을 수 있는 단어의 최대개수 answer
    answer = 0
    dfs(0, 5)
    # answer 출력
    print(answer)