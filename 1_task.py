def remainder_counter(remainder):
    count = 0
    if remainder == 1:
        count += 1
    elif remainder == 3 or 2:
        count += 2
    else:
        pass
    return count


counter = 0

spaces_amount = (int(input()) for _ in range(int(input())))
for space in spaces_amount:
    if space % 4 == 0:
        counter += space // 4
    else:
        counter += space // 4
        counter += remainder_counter(space % 4)

print(counter)
