import random


nums_1 = []
nums_2 = []

counter = 0
while counter < 10:
    nums_1.append(random.randint(1, 10))
    nums_2.append(random.randint(1, 10))
    counter += 1

unique_nums = list(set(nums_1 + nums_2))
print(unique_nums)
