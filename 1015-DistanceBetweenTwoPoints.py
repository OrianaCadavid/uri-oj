import math


def main():
    x1, y1 = raw_input().split()
    x1 = float(x1)
    y1 = float(y1)

    x2, y2 = raw_input().split()
    x2 = float(x2)
    y2 = float(y2)

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print '{:.4f}'.format(distance)


if __name__ == '__main__':
    main()
