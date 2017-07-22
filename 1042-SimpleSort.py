def main():
    a, b, c = map(int, input().split())

    if a > b and a > c and b > c:
        print(c)
        print(b)
        print(a)
        print()
        print(a)
        print(b)
        print(c)
    elif a > b and a > c and c > b:
        print(b)
        print(c)
        print(a)
        print()
        print(a)
        print(b)
        print(c)
    elif b > a and b > c and a > c:
        print(c)
        print(a)
        print(b)
        print()
        print(a)
        print(b)
        print(c)
    elif b > a and b > c and c > a:
        print(a)
        print(c)
        print(b)
        print()
        print(a)
        print(b)
        print(c)
    elif c > a and c > b and b > a:
        print(a)
        print(b)
        print(c)
        print()
        print(a)
        print(b)
        print(c)
    elif c > a and c > b and a > b:
        print(b)
        print(a)
        print(c)
        print()
        print(a)
        print(b)
        print(c)


if __name__ == '__main__':
    main()
