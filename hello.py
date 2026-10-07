import random


def roll_dice(sides=6, count=2):
    return [random.randint(1, sides) for _ in range(count)]


def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        else:
            yield str(i)


if __name__ == "__main__":
    rolls = roll_dice()
    print(f"Wuerfel: {rolls} (Summe: {sum(rolls)})")
    print(", ".join(fizzbuzz(15)))
