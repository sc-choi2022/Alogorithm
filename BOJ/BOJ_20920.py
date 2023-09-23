from collections import defaultdict
import sys

# 단어의 개수 N, 길이의 기준 M
N, M = map(int, sys.stdin.readline().split())
# 단어장 딕셔너리 memo
memo = defaultdict(int)

for _ in range(N):
    # 단어 word
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        memo[word] += 1
# 딕셔너리 memo를 list로 형변환
results = list(memo.items())
# 아래 조건에 맞게 정렬
# 1. 자주 나오는 단어일수록 앞에 배치
# 2. 해당 단어의 길이가 길수로 앞에 배치한다.
# 3. 알파벳 사진 순으로 배치
results.sort(key=lambda x:(-x[1],-len(x[0]), x[0]))
# 출력
for result in results:
    print(result[0])