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