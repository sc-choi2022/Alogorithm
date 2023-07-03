import sys

# 정수 A, B
A, B = map(int, sys.stdin.readline().split())
# 즐겨찾기 버튼의 개수 N
N = int(sys.stdin.readline())
shortcut = [int(sys.stdin.readline()) for _ in range(N)]
answer = 1000

# 즐겨찾기로 최소 버튼수를 확인
for i in range(N):
    answer = min(answer, abs(B-shortcut[i])+1)
# 주파수를 1MHz을 변경시킬 수 있는 경우에서 최소 버튼수를 확인
answer = min(answer, abs(B-A))
# 주파수 A에서 B로 갈 때 눌러야 하는 가장 적은 버튼수 출력
print(answer)