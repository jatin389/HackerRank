## https://www.hackerrank.com/challenges/3d-surface-area/copy-from/126293138


h,w= map(int,input().split())
row_Offset = 0
col_Offset=[0 for i in range(w)]

area = 2*(h*w)
for hh in range(h):
    arr = list(map(int,input().split()))

    row_Offset = 0
    for i in range(len(arr)):
        x = arr[i]
        tmp = x - row_Offset            # left to right (row wise)
        if(tmp > 0):
            area += 2 * tmp
        row_Offset = x

        tmp = x - col_Offset[i]         # top to bottom (column wise)
        if(tmp > 0):
            area += 2 * tmp
        col_Offset[i] = x

print(area)
