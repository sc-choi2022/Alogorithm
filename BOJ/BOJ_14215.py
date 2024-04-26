import sys

# 세 막대의 길이를 저장하는 배열 L
L = sorted(list(map(int, sys.stdin.readline().split())))

# 가장 큰 삼각혈의 둘레 출력
print(L[0]+L[1]+min(L[2], L[0]+L[1]-1))