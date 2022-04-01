# lst를 정렬된 두 리스트로 만든다.
def merge_sort(lst):
    if len(lst) == 1:
        return lst

    middle = len(lst)//2

    left = lst[:middle]
    right = lst[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

# 리스트 left와 right를 병합한다.
def merge(left, right):
    # 병합 과정에서 특정 경우의 수를 체크할 check
    global check
    # append를 사용하지 않기 위해서 length와 idx를 확인
    # left right 리스트의 길이 len_left, len_right
    # reuslt은 left와 right 길이의 합의 길이를 가진다.
    # left와 right의 idx위치 idx_left, idx_right 값 0 초기화
    len_left = len(left)
    len_right = len(right)
    result = [0]*(len_right+len_left)
    idx_left = 0
    idx_right = 0
    # result의 index 값 초기화
    i = 0
    # left의 마지막 원소가 right의 마지막 원소보다 큰 경우 check 1 증가
    if left[-1] > right[-1]:
        check += 1
    # 리스트 left나 right가 비어있지 않을 때
    while idx_left < len_left or idx_right < len_right:
        # left와 right모든 빈 리스트가 아닐 때 각 리스트의 첫 값을 비교하여 result에 추가
        if idx_left < len_left and idx_right < len_right:
            if left[idx_left] <= right[idx_right]:
                result[i] = left[idx_left]
                idx_left += 1
                i += 1
            else:
                result[i] = right[idx_right]
                idx_right += 1
                i += 1
        # left의 모든 값이 result에 추가된 경우
        elif idx_right < len_right:
            result[i] = right[idx_right]
            i += 1
            idx_right += 1
        # right의 모든 값이 result에 추가된 경우
        elif idx_left < len_left:
            result[i] = left[idx_left]
            i += 1
            idx_left += 1
    # 정렬이 완료된 리스트 result 반환
    return result

T = int(input())
for case in range(1, T+1):
    # 정렬 대상의 수 N
    N = int(input())
    # N개의 정렬 대상을 담은 리스트 lst
    lst = list(map(int, input().split()))
    # 병합 과정에서 left[-1] > right[-1]인 경우의 수 check 값 초기화
    check = 0
    # merge_sort를 통해 반환된 정렬리스트 result
    result = merge_sort(lst)
    # 테스트케이스 번호, N//2번째 값, 병합과정의 check 경우의 수 출력
    print(f'#{case} {result[N//2]} {check}')