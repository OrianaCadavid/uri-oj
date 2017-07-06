def main():
    db = {1: 4.0, 2: 4.5, 3: 5.0, 4: 2.0, 5: 1.50}

    code, quantity = raw_input().split()
    code = int(code)
    quantity = int(quantity)

    price = db[code] * quantity
    print 'Total: R$ {:.2f}'.format(price)


if __name__ == '__main__':
    main()
