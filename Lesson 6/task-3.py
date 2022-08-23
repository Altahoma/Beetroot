nums = [num for num in range(1, 100+1)]
result = []

counter = 0
while counter < 100:
    num = nums[counter]
    if num % 7 == 0 and num % 5 != 0:
        result.append(num)
    counter += 1

print(result)
