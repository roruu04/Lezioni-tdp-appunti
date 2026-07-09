def binomial(n, m):
    if m == 0 or m == n:
        return 1
    else:
        return binomial(n - 1, m - 1) + binomial(n - 1, m)


if __name__ == "__main__":
    n = 5
    m = 3
    print(binomial(n, m))