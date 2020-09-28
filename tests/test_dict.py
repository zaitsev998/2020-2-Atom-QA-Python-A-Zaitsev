from random import randint

import pytest


class TestDict:

    DICT_LENGTH = 5

    @pytest.mark.parametrize('key',
                             (2, DICT_LENGTH))
    def test_setdefault(self, key):
        dct = {i: i + 1 for i in range(self.DICT_LENGTH)}
        if key in dct:
            value = dct.setdefault(key, 'Lorem')
            assert value == key + 1
        else:
            value = dct.setdefault(key, 'Lorem')
            assert value == 'Lorem'

    def test_clear(self):
        dct = {i: i + 1 for i in range(self.DICT_LENGTH)}
        dct.clear()
        assert dct == {}

    @staticmethod
    def test_keys_is_immutable():
        dictionary = {}
        with pytest.raises(TypeError):
            assert dictionary[[1, 2, 3]]

    @pytest.mark.parametrize('key',
                             (2, DICT_LENGTH))
    def test_get(self, key):
        dct = {i: i + 1 for i in range(self.DICT_LENGTH)}
        if key in dct:
            assert dct.get(key) == key + 1
        else:
            assert dct.get(key) is None

    def test_zip_to_dict(self):
        list1 = [randint(i, i + 100) for i in range(self.DICT_LENGTH)]
        list2 = [randint(i + 100, i + 200) for i in range(self.DICT_LENGTH)]
        dict1 = dict(zip(list1, list2))
        dict2 = {list1[i]: list2[i] for i in range(min(len(list1), len(list2)))}
        assert dict1 == dict2
