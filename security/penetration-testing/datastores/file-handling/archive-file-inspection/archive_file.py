import unittest
import zipfile
import magic

class ArchiveFileInspectionTest(unittest.TestCase):
    def test_file_tux(self):
        filepath = 'data/demo.zip'
        file_type = magic.from_file(filepath, mime=True)
        print(f"The MIME type of '{filepath}' is: {file_type}")

    def test_zip(self):
        filepath = 'data/demo.zip'
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            # Listing all files and directories in the ZIP
            print("Contents of the ZIP file:")
            file_list = zip_ref.namelist()
            for file in file_list:
                info = zip_ref.getinfo(file)
                print(f"{info.filename} - Compressed Size: {info.compress_size} bytes, "
                    f"Uncompressed Size: {info.file_size} bytes, Date: {info.date_time}")



if __name__ == '__main__':
    unittest.main()
