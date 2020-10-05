from builtins import staticmethod
from random import randint

import pytest


class TestInt:

    @staticmethod
    def dec_to_oct(number):
        result = ''
        while number > 7:
            result = str(number % 8) + result
            number = number // 8
        result = str(number) + result
        result = '0o' + result
        return result

    @staticmethod
    @pytest.mark.parametrize(('number', 'result'),
                             ((5, 5),
                              (-6, 6)))
    def test_abs(number, result):
        assert abs(number) == result

    def test_oct(self):
        number = randint(1, 100)
        assert oct(number) == self.dec_to_oct(number)

    @staticmethod
    def test_int_is_immutable():
        num1 = randint(1, 1000)
        num2 = num1
        num1 += randint(1, 10)
        assert num1 is not num2

    @staticmethod
    def test_pow():
        number = randint(0, 100)
        exp = randint(0, 100)
        assert number ** exp == pow(number, exp)

    @staticmethod
    def test_divmod():
        number = randint(10, 100)
        denominator = randint(1, 9)
        assert divmod(number, denominator) == (number // denominator, number % denominator)
