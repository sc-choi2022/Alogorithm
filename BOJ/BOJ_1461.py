import sys

# 책의 개수 N와 한번에 들 수 있는 책의 개수 M
N, M = map(int, sys.stdin.readline().split())
# 책의 위치를 저장하는 books
books = sorted(list(map(int, sys.stdin.readline().split())))
