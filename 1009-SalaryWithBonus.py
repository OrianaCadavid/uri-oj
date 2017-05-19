def main():
    seller_name = str(raw_input())
    salary = float(raw_input())
    total_sales = float(raw_input())
    total_salary = salary + (total_sales * 0.15)
    print 'TOTAL = R$ {:.2f}'.format(total_salary)


if __name__ == '__main__':
    main()
