import sys
import os
from item_operations import create_item

def main_menu():
    filename='data.txt'
    for item in list(os.walk("./"))[0]:
        try:
            if filename not in item:
                with open(filename,'x+') as t:
                    t.write("")
        except FileExistsError:
            break
    while True:
        try:
            print('Please choose an item')
            print("1. Create a task")
            print("2. Update a task")
            print("3. Delete a task")
            print("4. View all tasks ")
            print("5. View open tasks")
            print("7. View finished tasks")
            print("8. Exit")
            print("="*80)
            user_input=float(input('Enter the number of the task you need to implement:\t'))
            
            if user_input==1:
                create_item(1,2,3,4)
            elif user_input==8:
                sys.exit()
            else:
                
                print("="*80)   
                print('Invalid Input')
                print("="*80)   
        except ValueError:
            print('Invalid Input')
            continue
        
if __name__ == '__main__':
    main_menu()