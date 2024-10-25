# import the file script to allow objects to be added to the list
import File

# The filesystem root
class FileSystem:
    def __init__(self):
        self.root = []

# creates a file using the name passed from main. Custom file extensions are allowed as well.
    def create_file(self, name):
        new_file = File.File(name)
        self.root.append(new_file)
        print(f'File {name} created successfully!')

# allows user to add content to files    
    def write_file(name, content):
        file = name.find_file(name)
        if file:
            file.content = content
            print(f'Content written to "{file.name}".')
        else:
            print(f'File "{name}" not found.')
# allows user to select a file to delete
    def delete_file(self, name):
        file = self.find_file(name)
        if file:
            self.files.remove(file)
            print(f'File "{name}" deleted.')
        else:
            print(f'File "{name}" not found.')

# searches for files using the file's name. when creating files, it also checks the extension.
    def search_files(self, name):
        for file in self.root:
            if file.name == name:
                return True
            else:
                return False
