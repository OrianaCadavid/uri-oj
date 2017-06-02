banknotes = [100, 50, 20, 10, 5, 2, 1]


def main():
    money = int(raw_input())
    print money
    for bn in banknotes:
        print '{} nota(s) de R$ {},00'.format(money / bn, bn)
        money = money % bn


if __name__ == '__main__':
    main()
