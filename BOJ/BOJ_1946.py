import sys
# 테스트케이스 T
T = int(sys.stdin.readline())

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