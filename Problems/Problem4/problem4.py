def largest_reverse_palindrome():
    res = 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            pr = i * j
            tmp = str(pr)[::-1]

            if str(pr) == tmp and pr > res:
                res = pr

    return res


if __name__ == "__main__":
    print(largest_reverse_palindrome())