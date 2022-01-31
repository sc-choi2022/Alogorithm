# 10번의 test를 위한 for문
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
            # sort()로 정렬
            height.sort()
            # 가장 작은 값인 index 0의 value를 더해줌
            view +=height[0]
	
    print(f'#{test_case} {view}')      