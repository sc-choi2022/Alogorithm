def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
    return answer

def dfs(lst, goal, idx, result):
    global answer
    # 모든 정수를 모두 사용한 경우
    if idx == len(lst):
        # 타켓 넘버를 만들 수 있는 경우
        if result == goal:
            answer += 1
        return
    dfs(lst, goal, idx+1, result-lst[idx])
    dfs(lst, goal, idx+1, result+lst[idx])

# 타켓 넘버를 만들 수 있는 방법의 수 answer
answer = 0