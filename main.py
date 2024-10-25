import FileSystem

def write_file(name, content):
    file = name.find_file(name)
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

    if base_choice in [1, 2, 3, 4, 5, 6]:
        return base_choice
    elif base_choice == 0:
        print("Here is a list of commands:")
        print('1. Create a file.')
        print('2. Read a file.')
        print('3. Write to a file.')
        print('4. Delete a file.')
        print('5. Show all files.')
        print('6. Exit.')
    else:
        print('Invalid selection. If you need a list of commands, enter 0.')
        return None


def create_file(filename, filesys):
    return None


def delete_file(self, name):
    file = self.find_file(name)
    if file:
        self.files.remove(file)
        print(f'File "{name}" deleted.')
    else:
        print(f'File "{name}" not found.')


def main():
    fs = FileSystem.FileSystem()

    while True:
        choice = get_input()
        if choice == 1:
            name = input("Enter a name for your file: ")
            extension = input('What file extension is it (without a period)? ')
            full_name = name + '.' + extension
            fs.create_file(full_name)

        elif choice == 2:
            return None
        elif choice == 3:
            filename = input("Enter the file name to write to: ")
            content = input("Enter the content: ")
            fs.write_file(filename, content)
        elif choice == 4:
            filename = input("Enter the file name to delete: ")
            fs.delete_file(filename)
        elif choice == 5:
            None
        elif choice is None:
            continue
        elif choice == 6:
            print('Goodbye!')
            break


if __name__ == "__main__":
    main()
