from random import randint

import pytest


class TestList:

    LIST_LENGTH = 5

    @pytest.mark.parametrize(('lst', 'elem', 'result'),
                             (([1, 2, 3, 4, 5], 6, 0),
                              ([1, 2, 3, 5, 3], 3, 2),
                              (['1', '2', '3'], '1', 1)))
    def test_count(self, lst, elem, result):
        assert lst.count(elem) == result

    def test_list_is_mutable(self):
        list1 = [i for i in range(self.LIST_LENGTH)]
        list2 = list1
        list1[0] = 6
        assert list1 is list2

    def test_insert(self):
        index = randint(0, self.LIST_LENGTH - 1)
        elem = randint(0, 100)
        list1 = [i for i in range(self.LIST_LENGTH)]
        list2 = list1[:index] + [elem] + list1[index:]
        list1.insert(index, elem)
        assert list1 == list2

    def test_clear(self):
        lst = [i for i in range(self.LIST_LENGTH)]
        lst.clear()
        assert lst == []

    def test_extend(self):
        list1 = [randint(i, i + 100) for i in range(self.LIST_LENGTH)]
        list2 = [randint(i + 100, i + 200) for i in range(self.LIST_LENGTH)]
        concatenated_list = list1 + list2
        list1.extend(list2)
        assert list1 == concatenated_list
