import unittest
import sqlite3

class LectureTest(unittest.TestCase):
    
    # TODO: Setup and Teardown 

    def test_query1(self):
        self.cur.execute('SELECT id,title,sws FROM lectures ORDER BY title')
        table = self.cur.fetchall()
        # Verify
        self.assertEqual(5, len(table))
        self.assertEqual((3,'Digital Electronics',4), table[0])
        self.assertEqual((1,'Mathematical Methods in Test Engineering',4), table[1])
        self.assertEqual((4,'Mixed-Signal Electronics',4), table[2])
        self.assertEqual((2,'Software Environments and Programming',4), table[3])
        self.assertEqual((5,'System Requirements and Testing',4), table[4])

    def test_query2(self):
        self.cur.execute("SELECT id,title,sws,ects FROM lectures WHERE title like '%Test%'")
        table = self.cur.fetchall()
        # Verify
        self.assertEqual(2, len(table))
        self.assertEqual((1,'Mathematical Methods in Test Engineering',4,6), table[0])
        self.assertEqual((5,'System Requirements and Testing',4,6), table[1])

    def test_delete(self):
        pass 
        # TODO

if __name__ == '__main__':
    unittest.main()
