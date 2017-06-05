def main():
    time = int(raw_input())
    hours = time / 3600
    time = time % 3600
    minutes = time / 60
    time = time % 60
    seconds = time

    print '{}:{}:{}'.format(hours, minutes, seconds)


if __name__ == '__main__':
    main()
