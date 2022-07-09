# A에 담기는 정수의 수 N
N = int(input())
# A를 set으로 설정하여 N개의 정수를 저장한다.
A = set(map(int, input().split()))
# 주어지는 M개의 정수
M = int(input())
# 순서가 중요하므로 list로 M개의 정수를 저장
lstM = list(map(int, input().split()))
# M을 순서에 맞에 확인하여 A에 있다면 1, 없다면 0 출력
for M in lstM:
    print(1 if M in A else 0)