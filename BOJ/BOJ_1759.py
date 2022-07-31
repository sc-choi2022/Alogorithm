import sys
# 암호 word, 사용한 알파벳의 idx, 모음개수 cnt을 매개변수로 하는 함수 dfs
def dfs(word, idx, cnt):
    # 암호가 완성되고 자음, 모음의 규칙이 맞다면 출력 후 return
    if len(word) == L and cnt > 0 and L-cnt > 1:
        print(word)
        return
    # 오름차순이 아니라면 return
    if len(word) > 1 and max(word) > word[-1]:
        return
    # 현재 조건으로 L의 길이를 만들 수 없다면 return
    if len(word)+len(lst[idx:]) < L:
        return

    for i in range(idx, C):
        if lst[i] not in word:
            if lst[i] in vowel:
                dfs(word+lst[i], i, cnt+1)
            else:
                dfs(word+lst[i], i, cnt)

# 암호를 이루는 알파벳 개수, 문자의 종류 가지수 C
L, C = map(int, sys.stdin.readline().split())
# C개의 문자들을 담는 리스트 lst
lst = sorted(list(sys.stdin.readline().split()))
# 모음을 담은 집합 vowel
vowel = set('aeiou')
# 빈문자열 암호와 idx, cnt을 0을 초기값으로 함수 dfs 실행
dfs('', 0, 0)