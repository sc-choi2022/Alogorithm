T = int(input())

for case in range(1, T+1):
    # 컨테이너의 수 N, 트럭의 수 M
    N, M = map(int, input().split())
    # N개의 컨테이너 화물 무게
    container = sorted(list(map(int, input().split())))
    # M개의 트럭 적재용량 무게
    truck = sorted(list(map(int, input().split())))

    # 큰 값부터 정렬
    container = container[::-1]
    truck = truck[::-1]
    # 사용할 수 있는 트럭의 위치를 표시할 변수 start 0으로 초기화
    start = 0
    # 컨데이너의 무게 ssum 값 0으로 초기화
    ssum = 0
    # 큰 무게부터 정렬된 컨테이너를
    for i in range(N):
        # 가용한 모든 트럭에서
        for j in range(start, len(truck)):
            # 무게를 비교하여 가능하면
            if container[i] <= truck[j]:
                # confirm 리스트에 cont[i] 추가하고 ssum에 컨데이너 무게를 추가
                ssum += container[i]
                # start 1 증가
                start += 1
                break

    # 테스트 케이스와 confirm 리스트 값의 합을 출력
    print(f'#{case} {ssum}')