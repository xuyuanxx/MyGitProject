#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest

# fixture 传递参数
# @pytest.fixture(params=[1, 2, 3, 'four'])
# def test_data(request):
#     return request.param
#
# def test_one(test_data):
#     print('\n hello test data: %s' % test_data)

# 参数化，前两个为变量，后面是对应的数据
# 3+5 --> test_input, 8-->expected
@pytest.mark.parametrize('test_input,expected', [('3+5', 8), ('6-1', 5), ('2*3', 6)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
