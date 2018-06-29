import sys
import math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
n = int(input())
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
for i in range(0, n//2):
    for j in range(0, n//2):
        for k in range(0, n//2):
            sum_all = i*5 + j*2 + k*3
            # 因为after a try, a transformation kick is played and is worth 2 extra points if successful条件的限制，所以try_times 必须大于等于tkick_times。
            if sum_all == n and i >= j:
                try_times = i
                tkick_times = j
                pkick_times = k
                # print(i, j, k, n, sum_all)
                print(str(try_times), str(tkick_times), str(pkick_times))
