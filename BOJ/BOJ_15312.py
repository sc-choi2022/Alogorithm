import sys
from collections import defaultdict

# 알파벳: 획수를 저장하는 딕셔너리 alphabet
alphabet = defaultdict(int)
# 알파벳의 획수를 저장한 배열 number
number = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
for i in range(26):
    alphabet[chr(65+i)] = number[i]
# 종민의 이름과 궁합을 볼 이름을 저장한 배열 A, B
A = list(sys.stdin.readline().rstrip())
B = list(sys.stdin.readline().rstrip())
# 이름의 길이 L
L = len(A)
# 이름의 궁합을 보기위한 배열 AB
AB = [[0]*(2*L) for _ in range(2*L-1)]
for j in range(L):
    AB[0][2*j] = alphabet[A[j]]
    AB[0][2*j+1] = alphabet[B[j]]
# 궁합의 결과 두자리 숫자까지 저장하는 for문
for ii in range(1, 2*L-1):
    for jj in range(ii, 2*L):
        AB[ii][jj] = (AB[ii-1][jj-1] + AB[ii-1][jj])%10
# 이름 궁합의 결과를 두 자리의 숫자로 출력
print(str(AB[2*L-2][2*L-2])+str(AB[2*L-2][2*L-1]))