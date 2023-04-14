def is_even(x: int) -> int:
    if x % 2 == 0:
        return True

    return False


def resolve(x: int) -> int:
    a = 1
    b = 2
    s = 0

    while a <= x:
        if is_even(a):
            s += a

        a, b = b, b + a

    return s


if __name__ == "__main__":
    print(resolve(4e6))