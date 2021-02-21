# -*- coding: utf-8 -*-
# @Author  : Ming
# @File    : test_calc.py
import pytest
import yaml

from python_code.calc import Calculator



with open("./calc.yaml") as f:
    datas = yaml.safe_load(f)['datas']
    add_datas = datas['add_datas']
    sub_datas = datas['sub_datas']
    mul_datas = datas['mul_datas']
    div_datas = datas['div_datas']
    myid = datas['myid']


class TestCalc:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize(
        "a, b, expect",
        add_datas, ids=myid
    )
    @pytest.mark.add
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相加结果之后写断言
        assert result == expect

    @pytest.mark.parametrize(
        "a, b, expect1",
        mul_datas, ids=myid
    )
    @pytest.mark.mul
    def test_mul(self, a, b, expect1):
        result = self.calc.mul(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相加结果之后写断言
        assert result == expect1

    @pytest.mark.parametrize(
        "a, b, expect1",
        sub_datas, ids=myid
    )
    @pytest.mark.sub
    def test_sub(self, a, b, expect1):
        result = self.calc.sub(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相加结果之后写断言
        assert result == expect1

    @pytest.mark.parametrize(
        "a, b, expect1",
        div_datas, ids=myid
    )
    @pytest.mark.div
    def test_div(self, a, b, expect1):
        result = self.calc.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相加结果之后写断言
        assert result == expect1