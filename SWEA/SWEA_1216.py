


# def & while문
import sys
# def check(arr):
#     # 리스트 arr의 전치행렬
#     trans_arr = list(zip(*arr))
#     # 가장 긴 회문 길이 max_len 초기화
#     M = 100
#     while M>0:
#         for i in range(100):
#             for j in range(100- M +1):
#                 temp1 = arr[i][j:j+M]
#                 temp2 = trans_arr[i][j:j+M]
#                 if temp1 == temp1[::-1]:
#                     return M
#                 if temp2 == temp2[::-1]:
#                     return M
#         M -= 1
#
#     return -1
#
# # 10번의 테스트 케이스
# for _ in range(10):
#     # 테스트 케이스 번호
#     case = int(input())
#     # 100 X 100 배열에 'A', 'B', 'C' 값을 담은 arr
#     arr = [list(input()) for _ in range(100)]
#
#     max_len = check(arr)
#     # 테스트 번호와 가장 긴 회문 길이 max_len 출력
#     print(f'#{case} {max_len}')

sys.stdin = open('input.txt')
# for문
for _ in range(10):
    # 테스트 케이스 번호
    case = int(input())
    # 100 X 100 배열에 'A', 'B', 'C' 값을 담은 arr
    arr = [list(input()) for _ in range(100)]
    # 리스트 arr의 전치행렬
    trans_arr = list(map(list, zip(*arr)))
    # 가장 긴 회문 길이 max_len 초기화
    max_len = 0

    # arr와 trans_arr의 모든 위치에 대해
    for i in range(100):
        for j in range(100):
            # 가장 긴 회문부터 가장 짧은 회문까지
            for M in range(100-j, -1, -1):
                # temp1, temp2로 임시 배열을 만들고
                temp1 = arr[i][j:j+M]
                temp2 = trans_arr[i][j:j+M]
                # 회문인지를 확인하고 회문이라면 길이를 max_len과 비교하여 할당
                if temp1 == temp1[::-1]:
                    if len(temp1) > max_len:
                        max_len = len(temp1)
                if temp2 == temp2[::-1]:
                    if len(temp2) > max_len:
                        max_len = len(temp2)
    # 테스트 번호와 가장 긴 회문 길이 max_len 출력
    print(f'#{case} {max_len}')