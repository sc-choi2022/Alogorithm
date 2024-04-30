import sys

# 키워드 개수 N, 글의 개수 M
N, M = map(int, sys.stdin.readline().split())
# 키워드를 저장하는 배열 keywords
keywords = set(sys.stdin.readline().rstrip() for _ in range(N))

for _ in range(M):
    writings = list(sys.stdin.readline().rstrip().split(','))
    for writing in writings:
        if writing in keywords:
            keywords.remove(writing)

    # x번째 줄에는 x번째 글을 쓰고 난 후에 메모장에 남아 있는 키워드의 개수를 출력
    print(len(keywords))