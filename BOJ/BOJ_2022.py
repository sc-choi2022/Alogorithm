import sys

def function(X, Y, W):
    h1 = (X**2 - W**2)**0.5
    h2 = (Y**2 - W**2)**0.5
    C = h1 * h2 / (h1 + h2)
    return C

X, Y, C = map(int, sys.stdin.readline().split())
