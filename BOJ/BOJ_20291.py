import sys

# 파일의 개수 N
N = int(sys.stdin.readline())

# 확장자의 종류를 저장하는 딕셔너리 file
file = {}

for _ in range(N):
    # 확장자 name
    name = sys.stdin.readline().rstrip().split('.')[1]
    # 딕셔너리 file에 name 반영
    if name in file:
        file[name] += 1
    else:
        file[name] = 1

# 확장자가 여러 개 있는 경우 확장자 이름의 사전순으로 출력
for l in sorted(file.items()):
    print(*l)