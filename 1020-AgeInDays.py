def main():
    age = int(raw_input())
    years = age / 365
    age = age % 365
    months = age / 30
    age = age % 30
    days = age

    print '{} ano(s)'.format(years)
    print '{} mes(es)'.format(months)
    print '{} dia(s)'.format(days)


if __name__ == '__main__':
    main()
