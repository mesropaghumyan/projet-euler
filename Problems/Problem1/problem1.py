def is_multiple(x: int) -> bool:
    if x % 3 == 0 or x % 5 == 0:
        return False

    return True


def sum(x: int) -> int:
    sum_value = 0

    for i in range(0, x):
        if not is_multiple(i):
            sum_value += i
            print(i)

    return sum_value


if __name__ == "__main__":
    print(sum(1000))
