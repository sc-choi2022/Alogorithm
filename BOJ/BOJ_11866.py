# 사람 수 N, 제거될 K번째
N, K = map(int, input().split())
# 원형으로 사용할 queue
queue = [ n for n in range( 1, N + 1) ]

# index로 사용하려고 하는
out = 0

print('<', end='')
while len(queue) > 1:
    # 제거될 index 위치
    out = (out + (K - 1)) % len(queue)
    # queue의 index위치의 값을 출력하고
    print(queue[out], end=', ')
    # queue에서 출력한 값을 제거한다.
    queue.remove(queue[out])
print(f'{queue[0]}>')