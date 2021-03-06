# 10번의 test를 위한 for문
# 첫번째 방법
for test_case in range(1, 10+1):
    len = int(input())
    data = list(map(int, input().split()))
    # 변수 초기화
    view = 0
    # 앞, 뒤 각각 2개를 비교하기 위해 양끝 2개씩 제외한 for문
    for i in range(2,len-2):
        if data[i] > data[i-2] and data[i] > data[i-1] and data[i] > data[i+1] and data[i] > data[i+2]:
            h1 = data[i] - data[i-2]
            h2 = data[i] - data[i-1]
            h3 = data[i] - data[i+1]
            h4 = data[i] - data[i+2]
            # 높이의 차이를 담은 list
            height = [h1, h2, h3, h4]

            # Bubble Sort를 통해 height를 정렬한다.
            for i in range(3, 0, -1):
                for j in range(0,i):
                    if height[j] > height[j+1]:
                        height[j], height[j+1] = height[j+1], height[j]

            # height의 가장 작은 값인 index 0의 value를 더해줌
            view +=height[0]
	
    print(f'#{test_case} {view}')

    # 두번째 방법
for case in range(1,10+1):
    N = int(input())
    bu = list(map(int, input().split()))
    cnt = 0

    # 앞, 뒤 각각 2개를 비교하기 위해 양끝 2개씩 제외한 for문
    for i in range(2, N-2):
        height = [bu[i-2], bu[i-1], bu[i+1], bu[i+2]]
        height.sort()
        # 주변의 값들이 현 위치보다 작다면 가장 큰 값과 현재의 값을 빼서 cnt에 더해준다.
        if height[-1] < bu[i]:
            cnt += bu[i] - height[-1]

    print(f'#{case} {cnt}')