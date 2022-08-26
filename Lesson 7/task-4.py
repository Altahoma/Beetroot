DAY_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# Dict comprehension
num_and_day = {num+1: day for num, day in enumerate(DAY_OF_WEEK)}
print(num_and_day)

# Reversed dict
day_and_num = {value: key for key, value in num_and_day.items()}
print(day_and_num)
