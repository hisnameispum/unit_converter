def main():
    print("*** Welcome to the Metric Conversion program ***")
    while True:
        choice = input('Enter units to convert, or \'Q\' to quit: ')
        if choice.upper() == 'Y' or choice.upper()== 'N':
            break
        print(f"Unrecognized units \"{choice}\", please try again")


main()