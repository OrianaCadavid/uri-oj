def main():
    code1, units1, price1 = raw_input().split()
    code1 = int(code1)
    units1 = int(units1)
    price1 = float(price1)

    code2, units2, price2 = raw_input().split()
    code2 = int(code2)
    units2 = int(units2)
    price2 = float(price2)

    cost = units1 * price1 + units2 * price2
    print 'VALOR A PAGAR: R$ {:.2f}'.format(cost)


if __name__ == '__main__':
    main()
