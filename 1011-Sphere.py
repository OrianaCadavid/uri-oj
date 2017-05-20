def main():
    PI = 3.14159
    radio = int(raw_input())
    volume = (4 / 3.0) * PI * (radio**3)
    print 'VOLUME = {:.3f}'.format(volume)


if __name__ == '__main__':
    main()
