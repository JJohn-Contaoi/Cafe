import datetime
# Dictionary List
coffee_list = {
    'espresso': {'large': 150, 'medium': 125, 'small': 100, 'sugar': range(0, 101, 25)},
    'cappuccino': {'large': 150, 'medium': 125, 'small': 100, 'sugar': range(0, 101, 25)},
    'latte': {'large': 150, 'medium': 125, 'small': 100, 'sugar': range(0, 101, 25)},
    'mocha': {'large': 150, 'medium': 125, 'small': 100, 'sugar': range(0, 101, 25)},
    'macchiato': {'large': 150, 'medium': 125, 'small': 100, 'sugar': range(0, 101, 25)},
    'americano': {'large': 150, 'medium': 125, 'small': 100, 'sugar': range(0, 101, 25)}
}
# display menu list
def coffee_menu():
    print('Menu list'.ljust(20) + 'large'.ljust(10) + 'medium'.ljust(10) + 'small'.ljust(10))
    print()
    for key, value in coffee_list.items():
        print(f'{key}'.ljust(21) + f'{value["large"]}'.ljust(10) + f'{value["medium"]}'.ljust(
            10) + f'{value["small"]}'.ljust(9))
    print('\nSugar level: 0-100%')
# list the customers order
purchased_items = []
new_purchased_items = []
# prompt a function for customer to purchase a coffee
def purchase_coffee(coffee_type, size, sugar_level):
    purchased_items.append({
        'coffee_type': coffee_type,
        'size': size,
        'sugar_level': sugar_level
    })
while True:
    coffee_menu()
    print()
    coffee_type = input("Enter coffee: ")
    if coffee_type not in coffee_list.keys():
        print("Coffee type not on the list please try again")
        input('\nPress Enter to continue...')
        continue
    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid input, please try again")
        input('\nPress Enter to continue...')
        continue
    while True:
        size = input("Enter size: ")
        if size not in coffee_list[coffee_type].keys():
            print("Invalid size please type only (large, medium, small)")
            input('\nPress Enter to continue...')
            continue
        try:
            sugar_level = int(input("Enter sugar level: "))
            if sugar_level not in coffee_list[coffee_type]['sugar']:
                print("Invalid input. Please type the range 0 to 100 in sequence of 25.")
                input('\nPress Enter to continue...')
                continue
        except ValueError:
            print("Invalid input, please type in range from 0 to 100")
            input('\nPress Enter to continue...')
            continue
        for i in range(quantity):
            purchase_coffee(coffee_type, size, sugar_level)
        print("Coffee purchased successfully")
        more = input("Do you want to purchase more? Type (y/n): ")
        if more.lower() == 'n':
            break
        else:
            if more.lower() == 'y':
                continue
            else:
                print('Invalid input. Proceed to the next function')
                input('\nPress Enter to continue...')
                break
    break
def remove_list():
    while True:
        if purchased_items == []:
            print('You have no current purchased.')
            input('\nPress Enter to continue and choose Add to order again...')
            break
        else:
            print('Current Purchased Items:')
            purchased_items.sort(key=lambda x: (x['coffee_type'], x['size'], x['sugar_level']))
            print('\n\t\tNo.'.ljust(8) + 'Menu List'.ljust(15) + 'Quantity'.ljust(12) + 'Size'.ljust(9) + 'Sugar')
            for item in purchased_items:
                if item not in new_purchased_items:
                    new_purchased_items.append(item)
            for i, item in enumerate(new_purchased_items):
                quantity = purchased_items.count(item)
                print('\t\t', f'{i + 1}.'.ljust(4) + f'{item["coffee_type"]}'.ljust(18) + f'{quantity}'.ljust(9) + f'{item["size"]}'.ljust(10) + f'{item["sugar_level"]}' + '%')
            try:
                remove_index = int(input("\nEnter the number of item you want to remove: "))
                if remove_index < 1:
                    raise ValueError
                if remove_index > len(new_purchased_items):
                    raise IndexError
            except ValueError:
                print("Invalid input. Please try again")
                input('\nPress Enter to continue...')
                continue
            except IndexError:
                print("Out of range Please try again")
                input('\nPress Enter to continue...')
                continue
            item = purchased_items[remove_index - 1]
            print('Current Purchased Items: ')
            for item in purchased_items:
                if item not in new_purchased_items:
                    new_purchased_items.append(item)
            print('\n\t\tQuantity'.ljust(16) + 'Menu List'.ljust(15) + 'Size'.ljust(9) + 'Sugar')
            for i, item in enumerate(new_purchased_items):
                if i == remove_index - 1:
                    quantity = purchased_items.count(item)
                    print('\t\t', f'{quantity:>3}'.ljust(12) + f'{item["coffee_type"]}'.ljust(15) +  f'{item["size"]}'.ljust(10) + f'{item["sugar_level"]}' + '%')
            total = 0
            for item in purchased_items:
                total += coffee_list[item['coffee_type']][item['size']]
            print('\n' + f'Total: {total}')
            try:
                remove_quantity = int(input(f'Enter quantity to remove from the purchase item (Max {quantity}): '))
                if remove_quantity > quantity:
                    print('Invalid quantity. Please try again')
                    input('\nPress Enter to continue...')
                    continue
                else:
                    for i in range(remove_quantity):
                        purchased_items.remove(item)
                    print('Your order have been removed successfully\n')
            except ValueError:
                print("Invalid input, please try again")
                input('\nPress Enter to continue...')
                continue
            response = input('Do you want to remove again? Type (y/n): ')
            if response.lower() == 'n':
                break
            else:
                if response.lower() == 'y':
                    continue
                else:
                    print('Invalid input. Proceed to the next function')
                    input('\nPress Enter to continue...')
                    break
    customer_choice()
def remove_all():
    purchased_items.clear()
    print('Orders removed successfully')
    input('\nPress Enter to continue...')
    customer_choice()
# creates a function for command list (view/add/remove/exit)
def customer_choice():
    print \
        ('''
        Type the Command list you want to do:

        View    -  to display the purchased list
        Add     -  to order another Menu
        Remove  -  to remove List/All the purchased list
        Exit    -  to end the app and display the transaction
        ''')
    choice = input("What do you want to do? ")
    # view the current purchased
    if choice.lower() == 'view':
        if len(purchased_items) == 0:
            print('You have no current purchased in your list.')
            input('\nPress Enter to continue and choose Add to order again...')
            customer_choice()
        else:
            print('Current Purchased Items: ')
            for item in purchased_items:
                if item not in new_purchased_items:
                    new_purchased_items.append(item)
            print('\n\t\tQuantity'.ljust(16) + 'Menu list'.ljust(15) + 'Size'.ljust(9) + 'Sugar')
            for item in new_purchased_items:
                quantity = purchased_items.count(item)
                print(f'\t\t{quantity:>4}'.ljust(15) + f'{item["coffee_type"]}'.ljust(14),
                      f'{item["size"]}'.ljust(9) + f'{item["sugar_level"]}' + '%')
            total = 0
            for item in purchased_items:
                total += coffee_list[item['coffee_type']][item['size']]
            print('\n' + f'Total: {total}')
        input('\nPress Enter to continue...')
        customer_choice()
    # make another purchase
    elif choice.lower() == 'add':
        while True:
            print()
            coffee_menu()
            print()
            coffee_type = input("Enter coffee: ")
            if coffee_type not in coffee_list.keys():
                print("Coffee type not on the list please try again")
                input('\nPress Enter to continue...')
                continue
            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid input, please try again")
                input('\nPress Enter to continue...')
                continue
            while True:
                size = input("Enter size: ")
                if size not in coffee_list[coffee_type].keys():
                    print("Invalid size please type only (large, medium, small)")
                    input('\nPress Enter to continue...')
                    continue
                try:
                    sugar_level = int(input("Enter sugar level: "))
                    if sugar_level not in coffee_list[coffee_type]['sugar']:
                        print("Invalid input. Please type the range 0 to 100 in sequence of 25.")
                        input('\nPress Enter to continue...')
                        continue
                except ValueError:
                    print("Invalid input, please type in range from 0 to 100")
                    input('\nPress Enter to continue...')
                    continue
                for i in range(quantity):
                    purchase_coffee(coffee_type, size, sugar_level)
                print("Coffee purchased successfully")
                more = input("Do you want to purchase more? Type (y/n): ")
                if more.lower() == 'n':
                    break
                else:
                    if more.lower() == 'y':
                        continue
                    else:
                        print('Invalid input. Proceed to the next function')
                        input('\nPress Enter to continue...')
                        customer_choice()
            break
        customer_choice()
    # remove the current purchased either remove (one/all)
    elif choice.lower() == 'remove':
        print \
            ('''
        Type the Command List (1/2):
        1. Remove List order you purchased
        2. Remove ALL the order you purchase
        ''')
        remove_choice = input('What do you want to do? ')
        if remove_choice.lower() == '1':
            remove_list()
        elif remove_choice.lower() == '2':
            remove_all()
        else:
            print('Invalid choice please proceed to command list')
            input('\nPress Enter to continue...')
            customer_choice()
    # calls the print purchase function
    elif choice.lower() == 'exit':
        if len(purchased_items) == 0:
            print \
                ('''
        ----------------- You have 0 current purchased ----------------
        --------------- Thank you for visiting our shop ---------------
        ---------------------- Amor de jose Cafe ----------------------
        ''')
            exit()
        else:
            total = 0
            for item in purchased_items:
                total += coffee_list[item['coffee_type']][item['size']]
            print('\n' + f'Total: {total}')
            try:
                money = int(input("Enter money: "))
                if money < total:
                    if input("Insufficient money. Do you want to continue? Type (y/n): ") == 'y':
                        customer_choice()
                    else:
                        print \
                            ('''
                    your current purchased have been removed due to lack of payment
                    --------------- Thank you for visiting our shop ---------------
                    ---------------------- Amor de jose Cafe ----------------------
                    ''')
                        exit()
                else:
                    date = datetime.datetime.now()
                    change = money - total
                    print \
                        ('\nReceipt:\n',
                         '\t\t' + 34 * '-' + '\n',
                         '\n')
                    print('\t\t' + 11 * '-', date.strftime('%d-%m-%Y'), 11 * '-')
                    print('\t\t' + 12 * '-', date.strftime("%H:%M:%S"), 12 * '-')
                    print \
                        ('\t\t' + 34 * '-' + '\n',
                         '\t\t' + 14 * '<' + ' MENU ' + 14 * '>' + '\n',
                         '\t\t' + 34 * '-' + '\n',
                         '\t\t', 'Purchased Items:'.ljust(20) + 'Size'.ljust(8) + 'Sugar')
                    for item in new_purchased_items:
                        quantity = purchased_items.count(item)
                        print('\t\t', f'{quantity}'.ljust(5) + f'{item["coffee_type"]}'.ljust(14),
                              f'{item["size"]}'.ljust(9) + f'{item["sugar_level"]}' + '%')
                    print \
                            ('\n\t\t' + 34 * '-',
                            '\n\t\t', 'Total:' + f'{total:>26}',
                            '\n\t\t', 'Money:' + f'{money:>26}',
                            '\n\t\t', 'Change:' + f'{change:>25}',
                            '\n\t\t' + 34 * '-' + '\n',
                            '\t\t Thank you for visiting our shop \n',
                            '\t\t------- Amor de jose Cafe --------')
                    exit()
            except ValueError:
                print('Invalid Input. Please proceed to Command List')
                input('\nPress Enter to continue...')
                customer_choice()
    else:
        print('Invalid choice please proceed to command list')
        input('\nPress Enter to continue...')
        customer_choice()
customer_choice()

# End of Code!
'''
features to be enlist soon  [maintenance] 

def limited_stocks():

def add_ons(): 

def new_product(): 

def buy2_get_freebies(): 

def list_number(): 

def customer_pending(): 

def cash_card(): 

def hot_cold():
'''