def gcd(a, b):
    if a == b:
        return a
    elif a == 1:
        return 1
    elif b == 1:
        return 1
    elif a / b > 1:
        if a % b == 0:
            return b
        else:
            a = a % b
            return gcd(a, b)
    elif b / a > 1:
        if b % a == 0:
            return a
        else:
            b = b % a
            return gcd(a, b)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()

