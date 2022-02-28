import sys
sys.stdin = open("GNS_test_input.txt")

test_case = int(input())
number_rule = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for _ in range(test_case):
    case, number_len = input().split()
    un_lst = list(input().split())
    or_lst = []

    for number in number_rule:
        for i in un_lst:
            if i == number:
                or_lst.append(i)
    print(case)
    print(*or_lst)

# 두번째 방법
sys.stdin = open('GNS_test_input.txt')

# 테스트케이스 개수
T = int(input())
# 행성의 0 ~ 9의 값을 순서대로 담은 리스트 num
num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for _ in range(10):
    # 케이스 번호와 테스트 케이스의 길이
    case, str_n = input().split()
    # 테스트 케이스 길이 int로 재할당
    str_n = int(str_n)

    # 정렬되지 않은 숫자들을 담은 리스트
    arr = list(input().split())
    # 인덱스 리스트 count
    count = [0]*10
    # 정렬된 숫자를 담을 리스트 초기화
    s_arr = [0]*len(arr)

    # 정렬되지 않는 리스트의 모든 값
    for i in range(len(arr)):
        # 행성 숫자들과 비교하여 인덱스리스트를 채운다.
        for j in range(10):
            if arr[i] == num[j]:
                count[j] += 1
    # 인덱스 리스트를 구성하기 위해 이전 값들을 더해 위치 값을 할당
    for c in range(1,10):
        count[c] += count[c-1]

    # arr의 마지막 값부터
    for ii in range(len(arr)-1, -1, -1):
        for j in range(10):
            # 리스트 num과 비교하고
            if arr[ii] == num[j]:
                # 인덱스 리스트를 확인하고 정렬 리스트에 값 할당
                count[j] -= 1
                s_arr[count[j]] = num[j]

    # 테스트 케이스의 번호와 정렬된 문자열 출력
    print(f'{case}')
    print(*s_arr)