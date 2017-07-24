def main():
    a, b, c = map(float, input().split())

    if a + b > c and a + c > b and b + c > a:
        perimeter_triangle = a + b + c
        print('Perimetro = {:.1f}'.format(perimeter_triangle))
    else:
        area_trapezium = 1 / 2 * c * (a + b)
        print('Area = {:.1f}'.format(area_trapezium))


if __name__ == '__main__':
    main()
