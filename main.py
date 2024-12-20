# Project: OS Filesystem simulation
# Members: Matthew Vrbka, Kadyn Van Hill, Takunda Mutore, Zach Myers, Brandt Murphy
# Repo link: https://github.com/JRatMain/OSFS
# 10-21 to 10-25, 2024

# importing filesystem class for creation and manipulation of a file system (using a list)
# this is a safe way of tinkering with 'files' without risking harm to the user's machine.
import FileSystem




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




# main function
def main():
    fs = FileSystem.FileSystem()
    fs_name = fs.name
    print(f'File system {fs_name} created.')
    while True:
        choice = get_input()
        if choice == 1:
            while True:
                name = input("Enter a name for your file: ")
                extension = input('What file extension is it (without a period)? ')
                full_name = name + '.' + extension
                file_found = fs.search_files(full_name)
                if file_found:
                    print('You cannot have the same name for new files.')
                    continue
                else:
                    break
            fs.create_file(full_name)

        elif choice == 2:
            filename = input('Enter the name of the file you want to read: ')
            fs.read_file(filename)

        elif choice == 3:
            filename = input("Enter the file name to write to: ")
            content = input("Enter the content: ")
            fs.write_file(filename, content)
        elif choice == 4:
            filename = input("Enter the file name to delete: ")
            fs.delete_file(filename)
        elif choice == 5:
            print("Files in the system:")
            fs.display_files()
        elif choice is None:
            continue
        elif choice == 6:
            print('Goodbye!')
            break


if __name__ == "__main__":
    main()
