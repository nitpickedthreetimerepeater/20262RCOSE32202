def main():
    print("math number evaluator")

    number = float(input("enter an answer: "))

    if number > 0 and number.is_integer():
        print("recommended: the answer is a natural number.")
    else:
        print("not recommended: the answer should be a natural number.")

if __name__ == "__main__":
    main()
