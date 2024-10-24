class File:
    def __init__(self, name):
        self.name = name
        self.content = ""

class FileSystem:
    def __init__(self):
        self.root = []



def write_file(self, name, content)
     file = self.find_file(name)
        if file:
            file.content = content
            print(f'Content written to "{file.name}".')
        else:
            print(f'File "{name}" not found.')

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


def main():
    fs = FileSystem()

while True:
        choice = get_input()
    if choice == 1:

    elif choice == 2:

    elif choice == 3:
        filename = input("Enter the file name to write to: ")
        content = input("Enter the content: ")
        fs.write_file(filename, content)
    elif choice == 4:

    elif choice == 5:

    elif choice is None:
        continue
    else:
        print("Exciting...")
        break

if __name__ == "__main__":
    main()