import sys

def round1(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

# 난이도 의견의 개수 N
N = int(sys.stdin.readline())
difficulty = sorted(int(sys.stdin.readline()) for _ in range(N))
# N의 15%값의 반올림 값 M
M = round1(N * .15)
# M의 값이 1보다 큰 경우 슬라이싱으로 difficulty 수정
difficulty = difficulty[M:-M] if M else difficulty
# solved.ac가 계산한 문제의 난이도를 출력
print(round1(sum(difficulty)/len(difficulty)) if difficulty else 0)