import os
import re
from unicodedata import normalize

class FileManager:
    BASE_DIRECTORY = "./doc"
    FILENAME_REGEX = r"^[a-zA-Z0-9 ]{1,25}\.?[a-zA-Z0-9]{0,3}$"
    FILENAME_PATTERN = re.compile(FILENAME_REGEX)

    def read_file(self, name):
        # Input validation
        if name is None:
            raise ValueError("File name cannot be None")

        normalized_name = normalize('NFKC', name)
        if not self.FILENAME_PATTERN.match(normalized_name):
            raise ValueError(f"Invalid file name: {name}")

        file_path = os.path.join(self.BASE_DIRECTORY, normalized_name)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except IOError as e:
            raise OSError(f"Can't access file {name}") from e


