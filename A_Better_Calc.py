def get_selection():
    selection_check = ["1", "2", "3", "4", "5", "addition", "subtraction", "multiplication", "division"]
    while True:
        try:
            num1 = int(input("Please input your first number: "))
            num2 = int(input("Please input your second number: "))
            break
        except ValueError:
            print("You entered a a word! Please enter a number!")
            continue
    while True:
        math_selection = input('''Please select a math operation from the following list. Type out the number or the type of addition.
        1: Addition
        2: Subtraction
        3: Multiplication
        4: Division
        (Choose one. Ex "1" Ex2 "Addition"): ''').lower()
        if math_selection not in selection_check:
            print("Please select something from the list")
            continue
        break
    return [num1, num2, math_selection]


def main():
    while True:
        selection = get_selection()
        if selection[2] == "1" or "addition":
            print((int(selection[0]) + int(selection[1])))
        if selection[2] == "2" or "subtraction":
            print(int(selection[0]-int(selection[1])))
        if selection[2] == "3" or "multiplication":
            print(int(selection[0])*int(selection[1]))
        if selection[2] == "4" or "division":
            pass  # Do Division
        again = input("Do you want to preform another operation? Y/n: ")
        if again.lower() == "n":
            break
main()
