import sys
sys.stdin = open("input.txt")

# solution 1
# 10개의 테스트케이스에 대한 for문
for test_case in range(10):
    # 변수 dump_num에 덤프 횟수 할당
    dump_num = int(input())
    # int map list를 활용하여 상자의 높이값들을 리스트 boxes에 할당
    boxes = list(map(int, input().split()))
    # 매 테스트마다의 max, min의 value 값을 초기화
    max_box, min_box = 0, 100

    # 덤프 수만큼 시행하는 for문
    for i in range(dump_num):
        # 매 덤프마다의 max, min의 값을 초기화
        max_box, min_box = 0, 100
        for box in boxes:
            if box > max_box:
                max_box = box
            if box < min_box:
                min_box = box

        # index 메소드를 이용하여 dump 내용을 반영
        boxes[boxes.index(max_box)] -= 1
        boxes[boxes.index(min_box)] += 1

    # 모든 작업 완료 후 값인 max_box, min_box 값 초기화
    max_box = 0
    min_box = 100

    # max와 min값을 구하기 위한 for문
    for box in boxes:
        if box > max_box:
            max_box = box
        if box < min_box:
            min_box = box

    # 테스트 케이스의 번호와 테스트 케이스의 최고점과 최저점의 높이 차 출력
    print(f'#{test_case+1} {max_box-min_box}')

# solution 2
# 10개의 테스트케이스에 대한 for문
for test_case in range(10):

    # 변수 dump_num에 덤프 횟수 할당
    dump_num = int(input())
    # int map list를 활용하여 상자의 높이값들을 리스트 boxes에 할당
    boxes = list(map(int, input().split()))
    # 매 테스트마다의 max, min의 index값과 value 값을 초기화

    for i in range(dump_num):
        # max와 min의 index와 value
        max_v = max(boxes)
        max_i = boxes.index(max_v)
        min_v = min(boxes)
        min_i = boxes.index(min_v)

        boxes[max_i] -= 1
        boxes[min_i] += 1

    # 테스트 케이스의 번호와 테스트 케이스의 최고점과 최저점의 높이 차 출력
    print(f'#{test_case + 1} {max(boxes) - min(boxes)}')