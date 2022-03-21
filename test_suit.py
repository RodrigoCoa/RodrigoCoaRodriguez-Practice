import unittest
from src.suit import Suit

class SuitTestMax(unittest.TestCase):
    def test_max(self):
        cal = Suit()
        result = cal.max(123)
        self.assertEqual(3, result)

    def test_max_negative(self):
        cal = Suit()
        result = cal.max(-899)
        self.assertFalse(result)

    def test_max_two_digits(self):
        cal = Suit()
        result = cal.max(99)
        self.assertFalse(result)

class SuitTestVocal(unittest.TestCase):
    def test_is_vocal_str(self):
        cal = Suit()
        result = cal.is_vowel('A')
        self.assertIs('Vowel', result)

    def test_is_vocal_num(self):
        cal = Suit()
        result = cal.is_vowel(5)
        self.assertIs('Num', result)

    def test_is_vocal_str_negative_num(self):
        cal = Suit()
        result = cal.is_vowel(-89)
        self.assertIs('Num', result)

    def test_is_vocal_consonant(self):
        cal = Suit()
        result = cal.is_vowel('c')
        self.assertIs('Consonant', result)

    def test_is_vocal_special_character(self):
        cal = Suit()
        result = cal.is_vowel('*')
        self.assertFalse(result)

class SuitTestInv(unittest.TestCase):
    def test_inv(self):
        cal = Suit()
        result = cal.inverse('AT16 Python')
        self.assertEqual('nohtyP 61TA', result)

    def test_inv_number(self):
        cal = Suit()
        result = cal.inverse(123)
        self.assertEqual(321, result)

    def test_inv_mixed(self):
        cal = Suit()
        result = cal.inverse('132a')
        self.assertEqual('a231', result)

class SuitTestPalindromo(unittest.TestCase):
    def test_palindromo(self):
        cal = Suit()
        result= cal.palindromo('ana')
        self.assertEqual('ana', result)

    def test_palindromo_number(self):
        cal = Suit()
        result= cal.palindromo(121)
        self.assertEqual(121, result)

    def test_palindromo_false(self):
        cal = Suit()
        result= cal.palindromo('acdf')
        self.assertFalse(result)

class SuitTestArray(unittest.TestCase):
    def test_array_max(self):
        cal = Suit()
        result = cal.array_max([2, 3, 4, 7])
        self.assertEqual(7, result)

    def test_array_min(self):
        cal = Suit()
        result = cal.array_min([10, -6, 5, 1])
        self.assertEqual(-6, result)

    def test_array_avg(self):
        cal = Suit()
        result = cal.array_avg([1, 2, 3, 4])
        self.assertEqual(2.5, result)

class SuitTestCountry(unittest.TestCase):
    def test_country(self):
        cal = Suit()
        result = cal.country(['España', 'Bolivia', 'Peru'])
        self.assertEqual('Bolivia', result)

    def test2_country(self):
        cal = Suit()
        result = cal.country(['España', 'Chile', 'Peru'])
        self.assertEqual('España', result)

    def test_country_empty(self):
        cal = Suit()
        result = cal.country([])
        self.assertFalse(result)

class SuitTestBinario(unittest.TestCase):
    def test_binario(self):
        cal = Suit()
        result = cal.binario(5)
        self.assertEqual(101, result)

    def test_binario_cero(self):
        cal = Suit()
        result = cal.binario(0)
        self.assertEqual(0, result)

    def test_binario_empty(self):
        cal = Suit()
        result = cal.binario("")
        self.assertFalse(result)

class SuitTestCont(unittest.TestCase):
    def test_cont(self):
        cal = Suit()
        result = cal.cont_string('abc')
        self.assertEqual(3, result)

    def test_cont_empty(self):
        cal = Suit()
        result = cal.cont_string('')
        self.assertEqual(0, result)

