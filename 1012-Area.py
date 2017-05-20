PI = 3.14159


def main():
    base, side, height = raw_input().split()
    base = float(base)
    side = float(side)
    height = float(height)

    area_triangle = 1 / 2.0 * (base * height)
    area_circle = PI * (height**2)
    area_trapezium = (1 / 2.0 * (base + side)) * height
    area_square = side * side
    area_rectangle = base * side
    print 'TRIANGULO: {:.3f}'.format(area_triangle)
    print 'CIRCULO: {:.3f}'.format(area_circle)
    print 'TRAPEZIO: {:.3f}'.format(area_trapezium)
    print 'QUADRADO: {:.3f}'.format(area_square)
    print 'RETANGULO: {:.3f}'.format(area_rectangle)


if __name__ == '__main__':
    main()
