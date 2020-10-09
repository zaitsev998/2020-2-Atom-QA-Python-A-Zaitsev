import pytest


class TestStr:

    @staticmethod
    @pytest.mark.parametrize(('string', 'sub', 'result'),
                             (('Lorem ipsum', 'em i', 3),
                             ('Lorem ipsum', 'lorem', -1)))
    def test_find(string, sub, result):
        assert string.find(sub) == result

    @staticmethod
    @pytest.mark.parametrize(('string', 'result'),
                             (('123', True),
                              ('   123    ', False),
                              ('Lorem ipsum', False),
                              ("123Lorem", False)))
    def test_isdigit(string, result):
        assert string.isdigit() is result

    @staticmethod
    def test_str_is_immutable():
        string = "Lorem ipsum"
        with pytest.raises(TypeError):
            string[2] = 'R'

    @staticmethod
    def test_lower():
        string = "Lorem IPSUM\n\t    "
        string_lower = string.lower()
        assert string_lower.islower()

    @staticmethod
    @pytest.mark.parametrize(('string', 'width', 'fillchar', 'result'),
                             (('Lorem', 3, '*', 'Lorem'),
                              ('Lorem', 7, '*', '**Lorem')))
    def test_rjust(string, width, fillchar, result):
        assert string.rjust(width, fillchar) == result
