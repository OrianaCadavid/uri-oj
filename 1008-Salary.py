def main():
    number = int(raw_input())
    worked_hours = int(raw_input())
    amount = float(raw_input())
    earned = worked_hours * amount
    print 'NUMBER = {}'.format(number)
    print 'SALARY = U$ {:.2f}'.format(earned)


if __name__ == '__main__':
    main()
