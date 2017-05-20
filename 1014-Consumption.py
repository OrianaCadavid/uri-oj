def main():
    distance = int(raw_input())
    spent_fuel = float(raw_input())
    consumption = distance / spent_fuel
    print '{:.3f} km/l'.format(consumption)


if __name__ == '__main__':
    main()
