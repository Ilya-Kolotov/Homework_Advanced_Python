from example import User
import unittest


class TestUnitCheck(unittest.TestCase):
    def setUp(self):
        self.user1 = User('Alex', 23, 2)
        self.user2 = User('Robert', 44, 3)
        self.another_user1 = User('Alex', 23, 2)

    def test_not_eq(self):
        self.assertFalse(self.user1 == self.user2)

    def test_eq(self):
        self.assertTrue(self.user1 == self.user1)

    def test_is(self):
        self.assertFalse(self.user1 is self.another_user1)

    def test_exist(self):
        with self.assertRaises(ValueError):
            User(1, 23, 1)
            User('Axel', 25, 9)
            User('Joe', -4, 5)

if __name__ == '__main__':
    unittest.main(verbosity=2)
