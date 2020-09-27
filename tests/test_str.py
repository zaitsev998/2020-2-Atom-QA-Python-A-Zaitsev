import pytest


class TestStr:

    @pytest.mark.parametrize(('string', 'sub', 'result'),
                             (('Lorem ipsum', 'em i', 3),
                             ('Lorem ipsum', 'lorem', -1)))
    def test_find(self, string, sub, result):
        assert string.find(sub) == result

    @pytest.mark.parametrize(('string', 'result'),
                             (('123', True),
                              ('   123    ', False),
                              ('Lorem ipsum', False),
                              ("123Lorem", False)))
    def test_isdigit(self, string, result):
        assert string.isdigit() is result

    def test_str_is_immutable(self):
        string = "Lorem ipsum"
        with pytest.raises(TypeError):
            string[2] = 'R'

    def test_lower(self):
        string = "Lorem IPSUM\n\t    "
        string_lower = string.lower()
        assert string_lower.islower()

    @pytest.mark.parametrize(('string', 'width', 'fillchar', 'result'),
                             (('Lorem', 3, '*', 'Lorem'),
                              ('Lorem', 7, '*', '**Lorem')))
    def test_rjust(self, string, width, fillchar, result):
        assert string.rjust(width, fillchar) == result
