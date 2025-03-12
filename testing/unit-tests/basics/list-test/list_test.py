import unittest

class ListTest(unittest.TestCase):
    def setUp(self):
        self.list = ['homer', 'marge', 'bart']

    def test_list_equal(self):
        expected = ['homer', 'marge', 'bart']
        self.assertListEqual(expected, self.list)

    def test_count_equal(self):
        expected = ['homer', 'marge', 'bart']
        self.assertCountEqual(expected, self.list)

    def test_list_index(self):
        self.assertEqual('marge', self.list[1])
        self.assertEqual('bart', self.list[-1])

    def test_list_size(self):
        # Exercise
        actual = len(self.list)
        # Verify
        expected = 3
        self.assertEqual(expected, actual)

    def test_list_modify_element(self):
        self.list[2] = 'lisa'
        expected = ['homer', 'marge', 'lisa']
        self.assertEqual(expected, self.list)

    def test_list_append(self):
        self.list.append('lisa')
        expected = ['homer', 'marge', 'bart', 'lisa']
        self.assertEqual(expected, self.list)

    def test_list_insert(self):
        self.list.insert(1,'lisa')
        expected = ['homer', 'lisa', 'marge', 'bart']
        self.assertEqual(expected, self.list)

    def test_list_delete_element(self):
        del self.list[1]
        expected = ['homer', 'bart']
        self.assertEqual(expected, self.list)

    def test_list_pop(self):
        string = self.list.pop()
        expected = ['homer', 'marge']
        self.assertEqual(expected, self.list)
        self.assertEqual('bart', string)

    def test_list_pop_with_index(self):
        string = self.list.pop(1)
        expected = ['homer', 'bart']
        self.assertEqual(expected, self.list)
        self.assertEqual('marge', string)

    def test_list_remove(self):
        self.list.remove('homer')
        expected = ['marge', 'bart']
        self.assertEqual(expected, self.list)

    def test_list_sort(self):
        self.list.sort()
        expected = ['bart', 'homer', 'marge']
        self.assertEqual(expected, self.list)

    def test_list_reverse(self):
        self.list.reverse()
        expected = ['bart', 'marge', 'homer']
        self.assertEqual(expected, self.list)

    def test_list_slice(self):
        sublist = self.list[1:2]  # [from:to)
        expected = ['marge']
        self.assertEqual(expected, sublist)

    def test_list_range(self):
        num_list = list(range(3,7))  # [from:to)
        expected = [3, 4, 5, 6]
        self.assertEqual(expected, num_list)


if __name__ == '__main__':
    unittest.main()
