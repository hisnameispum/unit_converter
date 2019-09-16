def from_meter(unit, value):
    converted_value = value * 3.28084
    converted_unit = '"'
    result = f"{value} meter(s) = {converted_value}{converted_unit}"
    print(result)

def from_mile(unit, value):
    converted_value = value * 1.609
    converted_unit = "km"
    result = f"{value} mile(s) = {converted_value}{converted_unit}"
    print(result)

def from_inch(unit, value):
    converted_value = value * 2.54
    converted_unit = "cm"
    result = f"{value}{unit} = {converted_value}{converted_unit}"
    print(result)


def main():
    print("*** Welcome to the Metric Conversion program ***")
    unit = ""
    converted_unit = ""
    value = 0
    converted_value = 0
    while True:
        choice = input('Enter units to convert, or \'Q\' to quit: ')
        if "ME" in choice.upper():
            keeper = choice.upper().split("ME")
            value = int(keeper[0])
            unit = "ME"
        elif "MI" in choice.upper():
            keeper = choice.upper().split("MI")
            value = int(keeper[0])
            unit = "MI"
        elif "'" in choice.upper():
            keeper = choice.upper().split("'")
            value = int(keeper[0])
            unit = "'"
        if unit.upper() == 'ME' or unit.upper()== 'MI' or unit.upper() == "'" or unit.upper() == "C" or unit.upper() == "F" or choice.upper() == "Q":
            break
        print(f"Unrecognized units \"{choice}\", please try again")
    while True:
        if unit == 'ME':
            from_meter(unit, value)
            break
        elif unit == 'MI':
            from_mile(unit, value)
            break
        elif unit == "'":
            from_inch(unit, value)
            break
        elif choice.upper() == "Q":
            print("Goodbye, and may you navigate smoothly through a world cluttered with competing standards.")
            break
    

main()