from __future__ import division


def main():
    distance_per_litre = 12
    time = int(raw_input())
    speed = int(raw_input())
    distance = time * speed
    fuel_spent = distance / distance_per_litre
    print '{:.3f}'.format(fuel_spent)


if __name__ == '__main__':
    main()
