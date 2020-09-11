from copy import deepcopy
from typing import List


def validate_without_order(actual: List[object], expect: List[object]):
    print('\n===========================================================')
    print('actual:', str(actual), '\nexpect:', str(expect))
    expect_copy = deepcopy(expect)
    for obj in actual:
        print('校验', obj, '是否存在于', expect_copy)
        assert obj in expect_copy
        expect_copy.remove(obj)
    assert len(expect_copy) == 0, "有未被使用的expect: " + str(expect_copy)
    print('===========================================================\n')


def validate(actual, expect):
    print('\n===========================================================')
    print('actual:', str(actual), '\nexpect:', str(expect))
    assert actual == expect
    print('===========================================================\n')
