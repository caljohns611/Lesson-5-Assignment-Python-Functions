#question 1 task 1
def addition():
    total_addition = (number_1 + number_2)
    print(f"Answer {total_addition}")

def subtraction():
    total_subtraction = (number_1 - number_2)
    print(f"Answer {total_subtraction}")

def multiplication():
    total_multiplicaion = (number_1 * number_2)
    print(f"Answer {total_multiplicaion}")

def division():
    total_division = (number_1 / number_2)
    print(f"Answer {total_division}")

#question 1 task 2
while True:
    action = input("Choose an action: [A]ddition, [S]ubtraction, [M]ultiplication, [D]ivision: ").upper()
    if action == 'A':
        number_1 = int(input("Enter a number: "))
        number_2 = int(input("Enter another number: "))
        addition()
    elif action == 'S':
        number_1 = int(input("Enter a number: "))
        number_2 = int(input("Enter another number: "))
        subtraction()
    elif action == 'M':
        number_1 = int(input("Enter a number: "))
        number_2 = int(input("Enter another number: "))
        multiplication()
    elif action == 'D':
        number_1 = int(input("Enter a number: "))
        number_2 = int(input("Enter another number: "))
        division()
    else:
        print("Invalid action. Please choose again.")