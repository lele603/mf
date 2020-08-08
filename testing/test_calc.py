import pytest
import yaml

from code.calc import Calcu

with open("./datas/cal.yaml", encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    adddata = datas['add']['adddata']
    addid = datas['add']['addid']
    divdata = datas['div']['divdata']
    divid = datas['div']['divid']


class TestCalc():

    def setup(self):
        print("开始计算")
        self.calc = Calcu()

    def teardown(self):
        print("结束计算")

    @pytest.mark.parametrize('a,b,respect', adddata, ids=addid)
    def test_add(self, a, b, respect):
        result = self.calc.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == respect

    @pytest.mark.parametrize('a,b,respect', divdata, ids=divid)
    def test_div(self, a, b, respect):
        result = self.calc.div(a, b)
        if b == 0:
            assert type(result) == type(respect)
        else:
            if isinstance(result, float):
                result = round(result, 3)
            assert result == respect
