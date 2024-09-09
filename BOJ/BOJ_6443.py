import sys

def dfs(idx, result):
    # 애너그램이 완성된 경우 출력
    if idx == L:
        print(result)
        return
    # 중복 없이 출력하기 위해 확인하는 변수 pre
    pre = ''
    for i in range(L):
        if pre != word[i] and not visit[i]:
            visit[i] = 1
            pre = word[i]
            dfs(idx+1, result+word[i])
            visit[i] = 0

# 단어의 개수 N
N = int(sys.stdin.readline())

for _ in range(N):
    # 주어지는 단어 word
    word = sorted(list(sys.stdin.readline().rstrip()))
    # word의 길이 L
    L = len(word)
    # word의 각 알파벳의 사용여부를 저장하는 배열 visit
    visit = [0] * L
    dfs(0, '')