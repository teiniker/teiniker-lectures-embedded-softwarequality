import os

class FileManager:
    BASE_DIRECTORY = "./doc"

    def read_file(self, name):
        if name is None:
            raise ValueError("File name cannot be None")

        file_path = os.path.join(self.BASE_DIRECTORY, name)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except IOError as e:
            raise OSError(f"Can't access file {name}") from e


