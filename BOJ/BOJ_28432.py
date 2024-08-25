import sys

# 기록의 길이 N
N = int(sys.stdin.readline())
# 기록을 저장하는 배열 records
records = list(sys.stdin.readline().rstrip() for _ in range(N))
# 후보 단어의 개수 M
M = int(sys.stdin.readline())
# 후보 단어를 저장하는 셋 candidates
candidates = set(sys.stdin.readline().rstrip() for _ in range(M))
# 찾아야하는 단어의 첫 문자 start, 단어의 마지막 문자 end
start, end = '', ''
for i in range(N):
    if records[i] == '?':
        if 0 < i:
            start = records[i-1][-1]
        if i+1 < N:
            end = records[i+1][0]
    else:
        if records[i] in candidates:
            candidates.remove(records[i])

candidates = list(candidates)

# 조건에 맞는 후보를 출력
for candidate in candidates:
    if start == '' and end == '':
        print(candidate)
        break
    elif start != '' and end == '':
        if candidate[0] == start:
            print(candidate)
            break
    elif start == '' and end != '':
        if candidate[-1] == end:
            print(candidate)
            break
    else:
        if candidate[0] == start and candidate[-1] == end:
            print(candidate)
            break