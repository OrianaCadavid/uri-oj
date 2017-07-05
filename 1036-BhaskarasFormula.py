import math


def main():
    a, b, c = map(float, raw_input().split())

    try:
        root1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        root2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        print 'R1 = {:.5f}'.format(root1)
        print 'R2 = {:.5f}'.format(root2)
    except (ZeroDivisionError, ValueError):
        print 'Impossivel calcular'


if __name__ == '__main__':
    main()
