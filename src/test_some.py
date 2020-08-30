#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest

# # 执行当前模块前自动执行（当前 module 特有的装饰器）
# @pytest.fixture(autouse=True, scope='module')
# def my_fixture():
#     print('module 初始化~~~')

# # 所有模块执行前执行yield前内容，所有模块执行后执行yield之后的内容（即使定义范围为 session 还是只作用于当前 module）
# @pytest.fixture(autouse=True, scope='session')
# def open():
#     print('打开浏览器~~~')
#     yield
#     print('关闭浏览器~~~')

def test_b():
    print('开始执行 test_b 方法')
    x = 'hello'
    assert 'e' in x
