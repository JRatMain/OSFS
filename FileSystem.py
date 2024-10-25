# import the file script to allow objects to be added to the list
import File

# The filesystem root
class FileSystem:
    def __init__(self):
        self.root = []
        self.name = 'root'

# creates a file using the name passed from main. Custom file extensions are allowed as well.
    def create_file(self, name):
        new_file = File.File(name)
        self.root.append(new_file)
        print(f'File {name} created successfully!')

# allows user to add content to files    
    def write_file(self, name, content):
        for file in self.root:
            if file.name == name:
                file.content = content
                print(f'Successfully wrote to {file.name}!')
                return
        print(f'File "{name}" not found.')
# allows user to select a file to delete
    def delete_file(self, name):
        for file in self.root:
            if file.name == name:
                self.root.remove(file)
                print(f'File "{name}" deleted.')
                return
        print(f'File "{name}" not found.')

# searches for files using the file's name. when creating files, it also checks the extension.
    def search_files(self, name):
        for file in self.root:
            if file.name == name:
                return True
            else:
                return False

    def display_files(self):
        if len(self.root) == 0:
            print('No files were found.')
            return
        for file in self.root:
            name = file.name
            print(name)
    def read_file(self, filename):
        if self.search_files(filename):
            for file in self.root:
                if file.name == filename:
                    file_data = file.content
                    print(file_data)
                    break