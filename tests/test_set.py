import pytest


class TestSet:

    first_set = {1, 3, 5, 7, 10}
    second_set = {2, 3, 5, 8, 12}

    def sets_definition(self):
        self.first_set = {1, 3, 5, 7, 10}
        self.second_set = {2, 3, 5, 8, 12}

    def test_union(self):
        self.sets_definition()
        assert self.first_set.union(self.second_set) == self.first_set | self.second_set

    def test_intersection(self):
        self.sets_definition()
        assert self.first_set.intersection(self.second_set) == self.first_set & self.second_set

    def test_difference(self):
        self.sets_definition()
        assert self.first_set.difference(self.second_set) == self.first_set - self.second_set

    def test_issubset(self):
        self.sets_definition()
        assert self.first_set.issubset(self.second_set) == (self.first_set <= self.second_set)

    @staticmethod
    @pytest.mark.parametrize(('init_set', 'item', 'result'),
                             (({'first', 'second'}, 'second', {'first'}),
                              ({'first', 'second'}, 'third', {'first', 'second'})))
    def test_discard(init_set, item, result):
        init_set.discard(item)
        assert init_set == result
