def fib_digit(n):
    a, b = 1, 1

    if n < 0:
        return 'Error'
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a, b = b, c % 10
        return b


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()