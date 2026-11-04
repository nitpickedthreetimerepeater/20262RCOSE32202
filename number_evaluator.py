def main():
    print("math number evaluator")
    print("1. answer")
    print("2. number in problem")
    print("3. number in solution")
    print("4. base of exponential or logarithmic function")
    print("5. leading coefficient of polynomial")

    number_type = input("select number type: ")
    number = float(input("enter a number: "))

    if number_type == "1":
        if number > 0 and number.is_integer():
            print("recommended: the answer is a natural number.")
        else:
            print("not recommended: the answer should be a natural number.")

    elif number_type == "2":
        if number.is_integer():
            print("recommended: the number is an integer.")
        else:
            print("not recommended: integers are preferred in problems.")

    elif number_type == "3":
        if number.is_integer():
            print("recommended: the number is an integer.")
        else:
            print("not recommended: integers are preferred in solutions.")

    elif number_type == "4":
        if number in [2, 3, 4]:
            print("recommended: the base is 2, 3, or 4.")
        elif number > 0 and number != 1:
            print("not recommended: 2, 3, or 4 is preferred.")
        else:
            print("invalid base: the base must be positive and not equal to 1.")

    elif number_type == "5":
        if number == 1:
            print("recommended: the leading coefficient is 1.")
        elif number == 0:
            print("invalid: the leading coefficient cannot be zero.")
        else:
            print("not recommended: a leading coefficient of 1 is preferred.")

    else:
        print("invalid number type.")


if __name__ == "__main__":
    main()
