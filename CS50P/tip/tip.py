def main():
    dollars = dollars_to_float(
        input("How much was the meal? ").replace("$", ""))
    print(dollars)
    percent = percent_to_float(
        input("What percentage would you like to tip? ").replace("%", ""))
    tip = dollars * percent * 0.01
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d)

def percent_to_float(p):
    return float(p)


main()
