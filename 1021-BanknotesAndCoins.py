import math

banknotes = [100, 50, 20, 10, 5, 2, 1]
coins = [50, 25, 10, 5, 1]


def main():
    money = float(raw_input())
    money_c, money_bn = math.modf(money)
    money_c = int(money_c * 100)
    money_bn = int(money_bn)

    ans_banknotes = {}
    ans_coins = {}
    for bn in banknotes:
        amount = money_bn / bn
        if bn == 1:
            ans_coins[100] = amount
        else:
            ans_banknotes[bn] = amount
        money_bn = money_bn % bn
    for c in coins:
        amount = money_c / c
        ans_coins[c] = amount
        money_c = money_c % c

    print 'NOTAS:'
    for bn in banknotes[:-1]:
        print '{} nota(s) de R$ {}.00'.format(ans_banknotes[bn], bn)
    print 'MOEDAS:'
    for c in [banknotes[-1] * 100] + coins:
        coin = c / 100.0
        print '{} moeda(s) de R$ {:.2f}'.format(ans_coins[c], coin)


if __name__ == '__main__':
    main()
