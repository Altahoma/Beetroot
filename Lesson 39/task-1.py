import asyncio


async def fibonacci(number):
    n1 = 0
    n2 = 1
    if number <= 0:
        raise ValueError("Number should be higher than 0.")
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    for i in range(2, number):
        temp = n1 + n2
        n1 = n2
        n2 = temp
    return n2


async def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result = result * i
    return result


async def square(number):
    return number**2


async def cubic(number):
    return number**3


async def main():
    funcs = [fibonacci, factorial, square, cubic]
    numbers = [num for num in range(1, 10)]

    for func in funcs:
        result = await asyncio.gather(*map(func, numbers))
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
