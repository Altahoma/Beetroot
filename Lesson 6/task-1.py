import random


numbers = []

counter = 0
while counter < 10:
    numbers.append(random.randint(0, 100))
    counter += 1

print(numbers)
print('max =', max(numbers))
