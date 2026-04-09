class TestFile:

    # Setup
    def setup_method(self):
        self.file = open('Sympathy.txt', 'rt', encoding="utf-8")

    # Teardown
    def teardown_method(self):
        self.file.close()

    def test_read_file(self):
        text = self.file.read()
        print(text)
        assert len(text) == 389

    def test_read_lines(self):
        lines = self.file.readlines()
        print(lines)
        assert len(lines) == 16

    def test_read_file_autoclose(self):
        with open('Sympathy.txt', 'rt', encoding="utf-8") as file:
            lines = file.readlines()
            print(lines)
            assert len(lines) == 16
