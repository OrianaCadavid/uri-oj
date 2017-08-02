def main():
    start, end = map(int, input().split())
    hours = (end - start + 24) % 24
    if hours == 0:
        hours = 24
    print('O JOGO DUROU {} HORA(S)'.format(hours))


if __name__ == '__main__':
    main()
