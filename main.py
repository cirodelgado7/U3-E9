import unittest
from Palindromo import Palindromo


class TestPalindromo(unittest.TestCase):
    __palindromo = None

    def setUp(self):
        self.__palindromo = Palindromo('Menem')

    def testPalindromoPar(self):
        self.__palindromo = Palindromo('Amorroma')

    def testUnNoPalindromo(self):
        self.__palindromo = Palindromo('Alejo')


if __name__ == '__main__':
    unittest.main()
