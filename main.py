from divide_number import divide


def is_leap_year(year):
    sum400 = divide(year, 400)
    sum4 = divide(year, 4)
    sum100 = divide(year, 100)

    if sum400.is_integer():
        print("400 rule")
        return True
    elif sum4.is_integer() and not sum100.is_integer():
        print("4 but not 100")
        return True
    else:
        return False


if __name__ == '__main__':
    print("-- Program to check whether a year is a leap year or not --")
    year = int(input("Enter a year: "))

    if is_leap_year(year):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


