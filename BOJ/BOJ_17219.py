import sys

# 저장된 사이트 주소의 수 N과 비밀번호를 찾으려는 사이트 주소의 수 M
N, M = map(int, sys.stdin.readline().split())
# 주소와 비밀번호를 저장하는 딕셔너리 info
info = {}

for _ in range(N):
    site, pwd = sys.stdin.readline().split()
    info[site] = pwd

for _ in range(M):
    # 비밀번호를 찾으려는 사이트 주소
    address = sys.stdin.readline().rstrip()
    # 비밀번호를 찾으려는 사이트 주소의 비밀번호 출력
    print(info[address])