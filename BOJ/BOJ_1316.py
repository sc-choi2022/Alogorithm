N = int(input())

cnt = 0
for _ in range(N):
    word = input()

    flag = False
    now = word[0]
    ans = set()
    ans.add(now)
    for i in range(1, len(word)):
        if now != word[i]:
            if word[i] not in ans:
                ans.add(word[i])
                now = word[i]
            elif word[i] in ans:
                flag = True
                break
    if flag == False:
        cnt += 1

print(cnt)