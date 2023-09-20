import sys

# 로그에 기록된 출입 기록의 수 N
N = int(sys.stdin.readline())
# 회사에 있는 사람의 배열 company
company = []

for _ in range(N):
    # 이름과 로그의 내용 name, log
    name, log = sys.stdin.readline().rstrip().split()
    # 출근인 경우
    if log == 'enter':
        company.append(name)
    # 퇴근인 경우
    else:
        company.remove(name)
# 사전 역순으로 정렬
company.sort(reverse=True)
# 사전 순의 역순으로 한 줄에 한 명씩 출력
for person in company:
    print(person)