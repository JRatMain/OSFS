
root = []
def getInput():
    prompt = 'Please enter a number: '

    baseChoice = int(input(prompt))
    if baseChoice == 1:
        return baseChoice
    elif baseChoice == 2:
        return baseChoice
    elif baseChoice == 3:
        return baseChoice
    elif baseChoice == 0:
        print("Here is a list of commands:")
        print('1. Create a file.')
        print('2. Delete a file.')
        print('3. Show all files.')
    else:
        print()
        print('Invalid selection. If you need a list of commands, enter 0.')



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


