
root = []
def get_input():
    prompt = 'Please enter a number 1-5 (0 for help): '
    
    try:
        base_choice = int(input(prompt))
    except ValueError:
        print('Invalid input. Please enter a number.')
        return None

    if base_choice in [1, 2, 3, 4, 5]:
        return base_choice
    elif base_choice == 0:
        print("Here is a list of commands:")
        print('1. Create a file.')
        print('2. Read a file.')
        print('3. Write to a file.')
        print('4. Delete a file.')
        print('5. Show all files.')
    else:
        print('Invalid selection. If you need a list of commands, enter 0.')
        return None



def welcome():
    dashes = '------------------------'
    equals = '========================'
    print(dashes)
    print(equals)
    print('Welcome to the OS Filesystem Simulation.')
    print('Your options are:')
    print()
    print('1. Create a file.')
    print('2. Delete a file.')
    print('3. Show all files.')
    print()
    print(equals)
    print(dashes)


def del_file():
    None

def mk_file():
    global root
    filename = input('Please enter the name of the file: ')
    full_name = filename + '.txt'


def show_files():
    None

if __name__ == "__main__":
    welcome()
    while (True):
        choice = getInput()
        if choice == 1:
            mk_file()
        elif choice == 2:
            del_file()
        elif choice == 3:
            show_files()
        else:
            raise Exception("Invalid choice number.")


