# 수열의 길이
N = int(input())
# 수열을 담은 리스트 arr
arr = list(map(int, input().split()))
# 수열을 반대로 담은 리스트 back_arr
back_arr = arr[::-1]
# 최대 길이와 첫 길이를 1로 초기화
max_len = 1
cnt = 1

# arr의 값들이 연속하여 증가한다면 cnt를 1 증가시키는 for문
for i in range(len(arr)-1):
    if arr[i] <= arr[i+1]:
        cnt += 1
    else:
        # 증가흐름이 멈추면 max_len과 비교하여 재설정
        if cnt > max_len:
            max_len = cnt
        cnt = 1
    if cnt > max_len:
        max_len = cnt
cnt = 1
# arr와 동일한 코드를 back_arr에 적용
for i in range(len(arr)-1):
    if back_arr[i] <= back_arr[i+1]:
        cnt += 1
    else:
        if cnt > max_len:
            max_len = cnt
        cnt = 1
    if cnt > max_len:
        max_len = cnt
# 수열의 가장 긴 길이 출력
print(max_len)