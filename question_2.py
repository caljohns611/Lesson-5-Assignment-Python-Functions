#question 2 task 1

shopping_list = []

def add_items(items):
    global shopping_list
    shopping_list.append(items)

#question 2 task 3
def display_shopping_list():
    global shopping_list
    print("Shopping list: ", end="\n\n")
    for items in shopping_list:
        if items == shopping_list[-1]:
            print(items)
        else:
            print(items, end=", ")
    print("\n")


while True:
    action = input("Choose an action: [A]dd an item, [D]isplay items, [R]emove item, [Q]uit: ").upper()
    if action == 'A':
        items = input("Enter the item: ")
        add_items(items)
    elif action == 'D':
        display_shopping_list()
        
    #question 2 taks 2
    elif action == 'R':
        item_remove = input("Enter the item you want to remove: ")
        if item_remove in shopping_list:
            shopping_list.remove(item_remove)
    elif action == 'Q':
        break
    else:
        print("Invalid action. Please choose again.")