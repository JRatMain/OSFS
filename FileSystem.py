import File

class FileSystem:
    def __init__(self):
        self.root = []

    def create_file(self, name):
        new_file = File.File(name)
        self.root.append(new_file)
        print(f'File {name} created successfully!')