import math

n, k, s = map(int, input().split())
dp = [int(i) for i in input().split()]

max_til_now = dp[0]
max_ending = 0
count = 1
result = 0
prev = None

for i in range(len(dp)):
    max_ending = max_ending + dp[i]

    if max_ending < 0:
        max_ending = 0

    elif max_til_now <= max_ending:
        if prev is None:
            prev = i
        count = len(dp[prev:i + 1])
        max_til_now = max_ending
        if result < (max_til_now - s * math.ceil(count / k)):
            result = max_til_now - s * math.ceil(count / k)


print(result)
