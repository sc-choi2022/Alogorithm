# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
chess = [1, 1, 2, 2, 2, 8]
# 찾은 흰색 킹, 퀸, 룩, 비숍, 나이트, 폰의 개수를 담은 리스트 found
found = list(map(int, input().split()))

# 입력에서 주어진 순서대로 몇 개의 피스를 더하거나 빼야 되는지를 출력
for i in range(len(chess)):
    print(chess[i] - found[i], end=' ')