import sys
# 테스트케이스 T
T = int(sys.stdin.readline())

# for문과 sort
for _ in range(T):
    # 지원자의 수 N
    N = int(sys.stdin.readline())
    # 지원자의 성적순위를 담을 리스트 people
    people = [0] * N

    for i in range(N):
        # 서류심사 성적 순위 t1, 면접성적 순위 t2
        t1, t2 = map(int, sys.stdin.readline().split())
        # people[i]에 각 값을 저장
        people[i] = [t1, t2]

    # people을 서류심사 성적 순위를 기준으로 정렬하여 peopleSort로 저장
    peopleSort = sorted(people, key=lambda x : x[0])
    # peopleSort의 0번째는 선발하므로 hired 1 증가
    hired = 1
    # 첫 선발 신입사원의 면접성적 순위값을 score에 저장
    score = peopleSort[0][1]

    # 정렬의 첫번째와 마지막을 제외한 모든 지원자를 확인
    for j in range(1, N):
        # poepleSort[j]의 면접성적 순위가 score보다 작은 경우
        if peopleSort[j][1] < score:
            # score값에 peopleSort[j][1] 저장
            score = peopleSort[j][1]
            # hired 1 증가
            hired += 1
    # 선발할 수 있는 신입사원 최대 인원수 출력
    print(hired)

# 코드 단순화
for _ in range(T):
    # 지원자의 수 N
    N = int(sys.stdin.readline())
    # 지원자의 정보
    people = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    people.sort(key=lambda x: (x[0], x[1]))
    mini = people[0]
    # 출력할 최대 인원
    maximum = N

    for i in range(1, N):
        if people[i][0] > mini[0] and people[i][1] > mini[1]:
            maximum -= 1
        else:
            mini = people[i]
    print(maximum)

# sort를 제거한 방법
for _ in range(T):
    # 지원자의 수 N
    N = int(sys.stdin.readline())
    # 성적을 담을 배열 grade
    grade = [0] * (N + 1)

    for _ in range(N):
        # 서류점수와 면접점수 paper, interview
        paper, interview = map(int, sys.stdin.readline().split())
        # 서류점수를 grade의 index로 하여 면접점수를 저장
        grade[paper] = interview
    # 서류점수 1등의 면접점수를 변수 limit에 저장
    limit = grade[1]
    # 출력할 최대 인원
    maximum = N

    for i in range(2, N + 1):
        # limit보다 면접점수가 낮은 경우 인원에 포함되지 않아 maximum 1 감소
        if grade[i] > limit:
            maximum -= 1
        # 인원에 포함되는 경우 limit값을 재설정
        else:
            limit = grade[i]
    # 선발할 수 있는 신입사원 최대 인원수 출력
    print(maximum)