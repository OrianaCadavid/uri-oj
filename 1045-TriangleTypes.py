def main():
    a, b, c = map(float, input().split())
    a, b, c = sorted([a, b, c], reverse=True)

    if a >= b + c:
        print('NAO FORMA TRIANGULO')
    elif a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO')
    elif a**2 > b**2 + c**2:
        print('TRIANGULO OBTUSANGULO')
    elif a**2 < b**2 + c**2:
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or c == a:
        print('TRIANGULO ISOSCELES')


if __name__ == '__main__':
    main()
