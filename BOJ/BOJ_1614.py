import sys

injured = int(sys.stdin.readline())
repeat = int(sys.stdin.readline())
ans = 0
hurtCnt = 0

if injured == 1:
    if repeat == 0:
        ans += injured - 1
    else:
        ans += 8 * repeat
elif injured == 5:
    if repeat == 0:
        ans += injured - 1
    else:
        ans += 4 + 8 * repeat
else:
    if repeat == 0:
        ans += injured - 1
    else:
        ans += 4 * repeat + 1
        if repeat % 2:
            ans += 4 - injured
        else:
            ans += injured - 2
print(ans)