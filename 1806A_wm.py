import sys
input = sys.stdin.readline
for _ in range(int(input())):
    ix,iy,tx,ty = map(int,input().split())
    x_len = tx - ix
    y_len = ty - iy
    if y_len < 0 or y_len < x_len :
        print(-1)
    else :
        print(y_len + abs(y_len-x_len))