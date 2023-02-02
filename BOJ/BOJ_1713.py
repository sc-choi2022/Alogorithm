import sys

# 사진틀의 개수 N
N = int(sys.stdin.readline())
# 추천 횟수 cnt
cnt = int(sys.stdin.readline())
# 추천받은 학생의 정보를 담을 배열 student
student = list(map(int, sys.stdin.readline().split()))
# 게시되는 학생 후보를 담을 딕셔너리 candidate
candidate = {}

for s in student:
    # s가 사진틀에 있는 경우
    if s in candidate:
    # if candidate.get(s):
        candidate[s] += 1
    # s가 사진틀에 없는 경우
    else:
        # 사진틀에 빈칸이 없는 경우
        if len(candidate) >= N:
            # 추천 횟수가 적고 오래된 후보를 제거
            candidate.pop(sorted(candidate.items(), key=lambda x: x[1])[0][0])
            # del(candidate[sorted(candidate.items(), key=lambda x: x[1])[0][0]])
        # 사진틀에 s을 추가
        candidate[s] = 1
# 사진틀에 사진이 게재된 최종 후보의 학생 번호를 증가하는 순서대로 출력
print(*sorted(candidate))