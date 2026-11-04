def main():
    print("math number evaluator")
    print("1. answer")
    print("2. number in problem")

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
            print("not recommended: integers are preferred.")

    else:
        print("invalid number type.")

if __name__ == "__main__":
    main()
