import math


def max_sublist_sum(a, k, s):
    max_sum = max_sum_current = 0
    for sublist_len in range(1, k+1):
        for i in range(len(a)-sublist_len+1):
            sublist = a[i:i+sublist_len]
            sublist_sum = sum(sublist)
            if sublist_sum > max_sum:
                max_sum = sublist_sum
                max_sum_current = sublist_sum
            else:
                max_sum_current = max(0, max_sum_current + sublist[-1] - sublist[0])
    return max_sum - s


def max_sublists(array, k, s):
    result = {}
    dp = [array[0]]

    for i in range(1, len(array)):
        dp_i = max(dp[i - 1] + array[i], array[i])
        dp.append(dp_i)

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            sublist_sum = sum(array[i:j + 1])
            sublist_len = j - i + 1
            if sublist_len < len(array):
                if sublist_len not in result:
                    result[sublist_len] = sublist_sum
                else:
                    result[sublist_len] = max(result[sublist_len], sublist_sum)

    for i in range(len(array) - 1):
        if i + 1 not in result:
            result[i + 1] = dp[i]
        else:
            result[i + 1] = max(result[i + 1], dp[i])

    return result


n, k, s = map(int, input().split())
dp = [int(i) for i in input().split()]

max_til_now = dp[0]
max_ending = 0
count = 1
result = 0
prev = None
reserve_dp = []

for i in range(len(dp)):
    max_ending = max_ending + dp[i]

    if max_ending < 0:
        max_ending = 0

    elif max_til_now <= max_ending:
        if prev is None:
            prev = i
        count = len(dp[prev:i + 1])
        reserve_dp = dp[prev:i + 1]
        max_til_now = max_ending
        if result < (max_til_now - s * math.ceil(count / k)):
            result = max_til_now - s * math.ceil(count / k)

results = max_sublists(reserve_dp)

if result < max_sublist_sum(reserve_dp, k, s):
    result = max_sublist_sum(reserve_dp, k, s)

for i in results:
    if result < (results[i] - s * math.ceil(i / k)):
        result = results[i] - s * math.ceil(i / k)

print(result)
